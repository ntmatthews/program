#!/usr/bin/env python3
"""
🗄️ PORTABLE DATABASE - USB Edition
===================================
A complete, self-contained database system that runs from USB.
No installation required - just plug and play!

Features:
- SQLite database (portable, no server needed)
- Full GUI interface
- Create/Read/Update/Delete records
- Multiple tables support
- Import/Export (CSV, JSON, Excel)
- Backup & Restore
- Search & Filter
- Password protection
- Runs on Windows, Mac, Linux
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import sqlite3
import json
import csv
import os
import sys
import hashlib
from datetime import datetime
import shutil

class PortableDatabase:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🗄️ Portable Database System - USB Edition")
        self.root.geometry("1200x700")
        
        # Get the directory where this script is running (USB drive)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "portable_data.db")
        self.config_path = os.path.join(self.base_dir, "config.json")
        
        self.conn = None
        self.current_table = None
        self.is_locked = True
        
        # Load or create config
        self.load_config()
        
        # Check password
        if self.config.get('password_enabled'):
            if not self.check_password():
                self.root.destroy()
                return
        
        self.is_locked = False
        self.init_database()
        self.create_gui()
        self.refresh_tables_list()
        
    def load_config(self):
        """Load configuration from JSON file"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'password_enabled': False,
                'password_hash': None,
                'auto_backup': True,
                'theme': 'default'
            }
            self.save_config()
    
    def save_config(self):
        """Save configuration to JSON file"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def check_password(self):
        """Check password if protection is enabled"""
        password = simpledialog.askstring("Password Required", 
                                         "Enter password to unlock database:", 
                                         show='*')
        if password is None:
            return False
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if password_hash == self.config['password_hash']:
            return True
        else:
            messagebox.showerror("Error", "Incorrect password!")
            return False
    
    def init_database(self):
        """Initialize database connection"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        
    def create_gui(self):
        """Create the main GUI interface"""
        # Set color scheme
        style = ttk.Style()
        style.theme_use('clam')
        
        # Top menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Table", command=self.create_table_dialog)
        file_menu.add_command(label="Import CSV", command=self.import_csv)
        file_menu.add_command(label="Import JSON", command=self.import_json)
        file_menu.add_separator()
        file_menu.add_command(label="Export Table (CSV)", command=self.export_csv)
        file_menu.add_command(label="Export Table (JSON)", command=self.export_json)
        file_menu.add_separator()
        file_menu.add_command(label="Backup Database", command=self.backup_database)
        file_menu.add_command(label="Restore Database", command=self.restore_database)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="SQL Query", command=self.sql_query_dialog)
        tools_menu.add_command(label="Set Password", command=self.set_password_dialog)
        tools_menu.add_command(label="Database Info", command=self.show_db_info)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Tables list
        left_panel = ttk.Frame(main_frame, width=200)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        ttk.Label(left_panel, text="Tables", font=('Arial', 14, 'bold')).pack(pady=(0, 10))
        
        # Tables listbox
        self.tables_listbox = tk.Listbox(left_panel, font=('Arial', 11))
        self.tables_listbox.pack(fill=tk.BOTH, expand=True)
        self.tables_listbox.bind('<<ListboxSelect>>', self.on_table_select)
        
        # Table buttons
        table_buttons_frame = ttk.Frame(left_panel)
        table_buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(table_buttons_frame, text="+ New", command=self.create_table_dialog).pack(side=tk.LEFT, padx=2)
        ttk.Button(table_buttons_frame, text="Delete", command=self.delete_table).pack(side=tk.LEFT, padx=2)
        
        # Right panel - Data view
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Toolbar
        toolbar = ttk.Frame(right_panel)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(toolbar, text="➕ Add Record", command=self.add_record_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="✏️ Edit Record", command=self.edit_record_dialog).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🗑️ Delete Record", command=self.delete_record).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🔄 Refresh", command=self.refresh_data).pack(side=tk.LEFT, padx=5)
        
        # Search bar
        search_frame = ttk.Frame(toolbar)
        search_frame.pack(side=tk.RIGHT, padx=5)
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self.filter_data())
        ttk.Entry(search_frame, textvariable=self.search_var, width=20).pack(side=tk.LEFT)
        
        # Data table with scrollbar
        table_frame = ttk.Frame(right_panel)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        h_scrollbar = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        
        # Treeview for data display
        self.data_tree = ttk.Treeview(table_frame, 
                                      yscrollcommand=v_scrollbar.set,
                                      xscrollcommand=h_scrollbar.set,
                                      selectmode='browse')
        
        v_scrollbar.config(command=self.data_tree.yview)
        h_scrollbar.config(command=self.data_tree.xview)
        
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.data_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_bar = ttk.Label(self.root, text="Ready | Database: portable_data.db", 
                                    relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def refresh_tables_list(self):
        """Refresh the list of tables"""
        self.tables_listbox.delete(0, tk.END)
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = cursor.fetchall()
        for table in tables:
            self.tables_listbox.insert(tk.END, table[0])
    
    def on_table_select(self, event):
        """Handle table selection"""
        selection = self.tables_listbox.curselection()
        if selection:
            self.current_table = self.tables_listbox.get(selection[0])
            self.load_table_data()
    
    def load_table_data(self):
        """Load data from selected table"""
        if not self.current_table:
            return
        
        # Clear existing data
        self.data_tree.delete(*self.data_tree.get_children())
        
        # Get column names
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({self.current_table})")
        columns = [col[1] for col in cursor.fetchall()]
        
        # Configure treeview columns
        self.data_tree['columns'] = columns
        self.data_tree['show'] = 'tree headings'
        
        self.data_tree.column('#0', width=50, anchor='center')
        self.data_tree.heading('#0', text='ID')
        
        for col in columns:
            self.data_tree.column(col, width=150, anchor='w')
            self.data_tree.heading(col, text=col)
        
        # Load data
        cursor.execute(f"SELECT rowid, * FROM {self.current_table}")
        rows = cursor.fetchall()
        
        for row in rows:
            self.data_tree.insert('', tk.END, text=row[0], values=row[1:])
        
        self.status_bar.config(text=f"Table: {self.current_table} | Records: {len(rows)}")
    
    def filter_data(self):
        """Filter displayed data based on search"""
        if not self.current_table:
            return
        
        search_term = self.search_var.get().lower()
        
        # Clear existing data
        self.data_tree.delete(*self.data_tree.get_children())
        
        # Get all data
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT rowid, * FROM {self.current_table}")
        rows = cursor.fetchall()
        
        # Filter and display
        for row in rows:
            row_str = ' '.join(str(x).lower() for x in row)
            if search_term in row_str:
                self.data_tree.insert('', tk.END, text=row[0], values=row[1:])
    
    def create_table_dialog(self):
        """Dialog to create a new table"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Create New Table")
        dialog.geometry("500x400")
        
        ttk.Label(dialog, text="Table Name:", font=('Arial', 11)).pack(pady=(10, 5))
        table_name_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=table_name_var, width=40).pack(pady=(0, 10))
        
        ttk.Label(dialog, text="Columns (one per line, format: name TYPE):", 
                 font=('Arial', 11)).pack(pady=(10, 5))
        
        columns_text = tk.Text(dialog, height=15, width=50)
        columns_text.pack(pady=(0, 10))
        columns_text.insert('1.0', 'name TEXT\nage INTEGER\nemail TEXT\ncreated_date TEXT')
        
        def create():
            table_name = table_name_var.get().strip()
            if not table_name:
                messagebox.showerror("Error", "Table name required!")
                return
            
            columns_def = columns_text.get('1.0', tk.END).strip()
            if not columns_def:
                messagebox.showerror("Error", "At least one column required!")
                return
            
            try:
                sql = f"CREATE TABLE {table_name} ({columns_def})"
                self.conn.execute(sql)
                self.conn.commit()
                self.refresh_tables_list()
                dialog.destroy()
                messagebox.showinfo("Success", f"Table '{table_name}' created!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create table: {e}")
        
        ttk.Button(dialog, text="Create Table", command=create).pack(pady=10)
    
    def delete_table(self):
        """Delete selected table"""
        if not self.current_table:
            messagebox.showwarning("Warning", "No table selected!")
            return
        
        if messagebox.askyesno("Confirm", f"Delete table '{self.current_table}'?"):
            try:
                self.conn.execute(f"DROP TABLE {self.current_table}")
                self.conn.commit()
                self.current_table = None
                self.data_tree.delete(*self.data_tree.get_children())
                self.refresh_tables_list()
                messagebox.showinfo("Success", "Table deleted!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete table: {e}")
    
    def add_record_dialog(self):
        """Dialog to add a new record"""
        if not self.current_table:
            messagebox.showwarning("Warning", "No table selected!")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Add Record to {self.current_table}")
        dialog.geometry("400x500")
        
        # Get columns
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({self.current_table})")
        columns = [(col[1], col[2]) for col in cursor.fetchall()]
        
        entries = {}
        
        for col_name, col_type in columns:
            frame = ttk.Frame(dialog)
            frame.pack(fill=tk.X, padx=20, pady=5)
            
            ttk.Label(frame, text=f"{col_name} ({col_type}):", width=20).pack(side=tk.LEFT)
            entry = ttk.Entry(frame, width=30)
            entry.pack(side=tk.LEFT, padx=10)
            entries[col_name] = entry
        
        def save():
            values = {k: v.get() for k, v in entries.items()}
            placeholders = ', '.join(['?' for _ in values])
            columns_str = ', '.join(values.keys())
            
            try:
                sql = f"INSERT INTO {self.current_table} ({columns_str}) VALUES ({placeholders})"
                self.conn.execute(sql, list(values.values()))
                self.conn.commit()
                self.load_table_data()
                dialog.destroy()
                messagebox.showinfo("Success", "Record added!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add record: {e}")
        
        ttk.Button(dialog, text="Save Record", command=save).pack(pady=20)
    
    def edit_record_dialog(self):
        """Dialog to edit selected record"""
        if not self.current_table:
            messagebox.showwarning("Warning", "No table selected!")
            return
        
        selection = self.data_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "No record selected!")
            return
        
        item = self.data_tree.item(selection[0])
        rowid = item['text']
        values = item['values']
        
        dialog = tk.Toplevel(self.root)
        dialog.title(f"Edit Record (ID: {rowid})")
        dialog.geometry("400x500")
        
        # Get columns
        cursor = self.conn.cursor()
        cursor.execute(f"PRAGMA table_info({self.current_table})")
        columns = [col[1] for col in cursor.fetchall()]
        
        entries = {}
        
        for i, col_name in enumerate(columns):
            frame = ttk.Frame(dialog)
            frame.pack(fill=tk.X, padx=20, pady=5)
            
            ttk.Label(frame, text=f"{col_name}:", width=20).pack(side=tk.LEFT)
            entry = ttk.Entry(frame, width=30)
            entry.insert(0, values[i])
            entry.pack(side=tk.LEFT, padx=10)
            entries[col_name] = entry
        
        def save():
            new_values = {k: v.get() for k, v in entries.items()}
            set_clause = ', '.join([f"{k} = ?" for k in new_values.keys()])
            
            try:
                sql = f"UPDATE {self.current_table} SET {set_clause} WHERE rowid = ?"
                self.conn.execute(sql, list(new_values.values()) + [rowid])
                self.conn.commit()
                self.load_table_data()
                dialog.destroy()
                messagebox.showinfo("Success", "Record updated!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update record: {e}")
        
        ttk.Button(dialog, text="Save Changes", command=save).pack(pady=20)
    
    def delete_record(self):
        """Delete selected record"""
        if not self.current_table:
            messagebox.showwarning("Warning", "No table selected!")
            return
        
        selection = self.data_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "No record selected!")
            return
        
        item = self.data_tree.item(selection[0])
        rowid = item['text']
        
        if messagebox.askyesno("Confirm", f"Delete record ID {rowid}?"):
            try:
                self.conn.execute(f"DELETE FROM {self.current_table} WHERE rowid = ?", (rowid,))
                self.conn.commit()
                self.load_table_data()
                messagebox.showinfo("Success", "Record deleted!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete record: {e}")
    
    def refresh_data(self):
        """Refresh the current table data"""
        if self.current_table:
            self.load_table_data()
    
    def import_csv(self):
        """Import data from CSV file"""
        filepath = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if not filepath:
            return
        
        table_name = simpledialog.askstring("Table Name", "Enter table name for imported data:")
        if not table_name:
            return
        
        try:
            with open(filepath, 'r') as f:
                reader = csv.DictReader(f)
                columns = reader.fieldnames
                
                # Create table
                columns_def = ', '.join([f"{col} TEXT" for col in columns])
                self.conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})")
                
                # Insert data
                for row in reader:
                    placeholders = ', '.join(['?' for _ in columns])
                    columns_str = ', '.join(columns)
                    sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
                    self.conn.execute(sql, [row[col] for col in columns])
                
                self.conn.commit()
                self.refresh_tables_list()
                messagebox.showinfo("Success", f"Imported data into table '{table_name}'!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import CSV: {e}")
    
    def import_json(self):
        """Import data from JSON file"""
        filepath = filedialog.askopenfilename(
            title="Select JSON File",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if not filepath:
            return
        
        table_name = simpledialog.askstring("Table Name", "Enter table name for imported data:")
        if not table_name:
            return
        
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, list):
                messagebox.showerror("Error", "JSON must be an array of objects!")
                return
            
            if len(data) == 0:
                messagebox.showerror("Error", "JSON file is empty!")
                return
            
            # Get columns from first object
            columns = list(data[0].keys())
            columns_def = ', '.join([f"{col} TEXT" for col in columns])
            self.conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def})")
            
            # Insert data
            for row in data:
                placeholders = ', '.join(['?' for _ in columns])
                columns_str = ', '.join(columns)
                sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
                self.conn.execute(sql, [row.get(col, '') for col in columns])
            
            self.conn.commit()
            self.refresh_tables_list()
            messagebox.showinfo("Success", f"Imported data into table '{table_name}'!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import JSON: {e}")
    
    def export_csv(self):
        """Export current table to CSV"""
        if not self.current_table:
            messagebox.showwarning("Warning", "No table selected!")
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if not filepath:
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {self.current_table}")
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(columns)
                writer.writerows(rows)
            
            messagebox.showinfo("Success", f"Exported to {filepath}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export CSV: {e}")
    
    def export_json(self):
        """Export current table to JSON"""
        if not self.current_table:
            messagebox.showwarning("Warning", "No table selected!")
            return
        
        filepath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if not filepath:
            return
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {self.current_table}")
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            
            data = [dict(zip(columns, row)) for row in rows]
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            
            messagebox.showinfo("Success", f"Exported to {filepath}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export JSON: {e}")
    
    def backup_database(self):
        """Create a backup of the database"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}.db"
        backup_path = os.path.join(self.base_dir, backup_name)
        
        try:
            shutil.copy2(self.db_path, backup_path)
            messagebox.showinfo("Success", f"Backup created: {backup_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create backup: {e}")
    
    def restore_database(self):
        """Restore database from backup"""
        filepath = filedialog.askopenfilename(
            title="Select Backup File",
            filetypes=[("Database files", "*.db"), ("All files", "*.*")]
        )
        
        if not filepath:
            return
        
        if messagebox.askyesno("Confirm", "This will replace your current database. Continue?"):
            try:
                self.conn.close()
                shutil.copy2(filepath, self.db_path)
                self.conn = sqlite3.connect(self.db_path)
                self.conn.row_factory = sqlite3.Row
                self.refresh_tables_list()
                self.data_tree.delete(*self.data_tree.get_children())
                messagebox.showinfo("Success", "Database restored!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to restore database: {e}")
    
    def sql_query_dialog(self):
        """Execute custom SQL query"""
        dialog = tk.Toplevel(self.root)
        dialog.title("SQL Query")
        dialog.geometry("600x400")
        
        ttk.Label(dialog, text="Enter SQL Query:", font=('Arial', 11)).pack(pady=10)
        
        query_text = tk.Text(dialog, height=10, width=70)
        query_text.pack(pady=10)
        
        result_text = tk.Text(dialog, height=10, width=70)
        result_text.pack(pady=10)
        
        def execute():
            query = query_text.get('1.0', tk.END).strip()
            try:
                cursor = self.conn.cursor()
                cursor.execute(query)
                
                if query.strip().upper().startswith('SELECT'):
                    rows = cursor.fetchall()
                    result_text.delete('1.0', tk.END)
                    result_text.insert('1.0', f"Results ({len(rows)} rows):\n\n")
                    for row in rows:
                        result_text.insert(tk.END, f"{dict(row)}\n")
                else:
                    self.conn.commit()
                    result_text.delete('1.0', tk.END)
                    result_text.insert('1.0', f"Query executed successfully!\nRows affected: {cursor.rowcount}")
                    self.refresh_tables_list()
                    if self.current_table:
                        self.load_table_data()
            except Exception as e:
                result_text.delete('1.0', tk.END)
                result_text.insert('1.0', f"Error: {e}")
        
        ttk.Button(dialog, text="Execute Query", command=execute).pack(pady=10)
    
    def set_password_dialog(self):
        """Set or change password"""
        password = simpledialog.askstring("Set Password", 
                                         "Enter new password (leave empty to disable):", 
                                         show='*')
        
        if password is None:
            return
        
        if password == '':
            self.config['password_enabled'] = False
            self.config['password_hash'] = None
            messagebox.showinfo("Success", "Password protection disabled!")
        else:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.config['password_enabled'] = True
            self.config['password_hash'] = password_hash
            messagebox.showinfo("Success", "Password set successfully!")
        
        self.save_config()
    
    def show_db_info(self):
        """Show database information"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        total_records = 0
        table_info = []
        
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            total_records += count
            table_info.append(f"  • {table_name}: {count} records")
        
        db_size = os.path.getsize(self.db_path) / 1024  # KB
        
        info = f"""Database Information:
        
Location: {self.db_path}
Size: {db_size:.2f} KB
Tables: {len(tables)}
Total Records: {total_records}

Tables:
{chr(10).join(table_info)}

Password Protection: {"Enabled" if self.config['password_enabled'] else "Disabled"}
"""
        
        messagebox.showinfo("Database Info", info)
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About", 
"""🗄️ Portable Database System v1.0

A complete, self-contained database that runs from USB.
No installation required - just plug and play!

Features:
• SQLite database (portable)
• Full CRUD operations
• Import/Export (CSV, JSON)
• Backup & Restore
• Password protection
• Cross-platform (Windows, Mac, Linux)

Perfect for:
• Portable data management
• Offline databases
• Quick prototyping
• Personal projects
• Small business data

Created for easy, portable data management!""")
    
    def run(self):
        """Start the application"""
        if not self.is_locked:
            self.root.mainloop()
            if self.conn:
                self.conn.close()

if __name__ == "__main__":
    app = PortableDatabase()
    app.run()
