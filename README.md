# 🗄️ PORTABLE DATABASE - USER GUIDE

## What Is This?

A **complete, self-contained database system** that runs entirely from a USB drive. No installation needed - just plug in your USB and run!

## ✨ Features

### Core Functionality
✅ **SQLite Database** - Fast, reliable, no server needed  
✅ **Full GUI Interface** - Easy point-and-click  
✅ **CRUD Operations** - Create, Read, Update, Delete  
✅ **Multiple Tables** - Organize different types of data  
✅ **Search & Filter** - Find data quickly  

### Import/Export
✅ **CSV Import/Export** - Work with spreadsheets  
✅ **JSON Import/Export** - Exchange data with apps  
✅ **Backup & Restore** - Protect your data  

### Security
✅ **Password Protection** - Lock your database  
✅ **Portable** - Runs on any computer  
✅ **No Internet Required** - 100% offline  

## 🚀 Quick Start

### First Time Setup

1. **Copy to USB Drive**
   ```
   Copy the entire folder to your USB drive
   ```

2. **Run the Launcher**
   - **Windows**: Double-click `launch.bat`
   - **Mac/Linux**: Double-click `launch.sh` (make executable first)
   - **Or**: Run `python3 portable_database.py`

3. **Create Your First Table**
   - Click "File" → "New Table"
   - Name it (e.g., "contacts")
   - Add columns:
     ```
     name TEXT
     email TEXT
     phone TEXT
     notes TEXT
     ```
   - Click "Create Table"

4. **Add Data**
   - Select your table from the left panel
   - Click "➕ Add Record"
   - Fill in the fields
   - Click "Save Record"

## 📋 Common Use Cases

### 1. Contact Manager
```
Table: contacts
Columns:
  - name TEXT
  - email TEXT
  - phone TEXT
  - company TEXT
  - notes TEXT
```

### 2. Inventory Tracker
```
Table: inventory
Columns:
  - item_name TEXT
  - quantity INTEGER
  - price REAL
  - location TEXT
  - last_updated TEXT
```

### 3. Task Manager
```
Table: tasks
Columns:
  - task TEXT
  - priority TEXT
  - status TEXT
  - due_date TEXT
  - notes TEXT
```

### 4. Password Vault
```
Table: passwords
Columns:
  - service TEXT
  - username TEXT
  - password TEXT
  - url TEXT
  - notes TEXT

Important: Set a database password!
Tools → Set Password
```

### 5. Student Records
```
Table: students
Columns:
  - student_id TEXT
  - name TEXT
  - grade TEXT
  - email TEXT
  - phone TEXT
```

## 🎯 How To Use

### Creating Tables

1. Click **File → New Table**
2. Enter table name (e.g., "customers")
3. Define columns (one per line):
   ```
   name TEXT
   age INTEGER
   email TEXT
   joined_date TEXT
   ```
4. Click **Create Table**

**Column Types:**
- `TEXT` - Text/strings
- `INTEGER` - Whole numbers
- `REAL` - Decimal numbers
- `BLOB` - Binary data

### Adding Records

1. Select a table from the left panel
2. Click **➕ Add Record**
3. Fill in all fields
4. Click **Save Record**

### Editing Records

1. Select a record in the table
2. Click **✏️ Edit Record**
3. Modify the fields
4. Click **Save Changes**

### Deleting Records

1. Select a record in the table
2. Click **🗑️ Delete Record**
3. Confirm the deletion

### Searching Data

1. Use the **Search** box in the toolbar
2. Type any text to filter results
3. Search looks through all columns

### Importing Data

**From CSV:**
1. Click **File → Import CSV**
2. Select your CSV file
3. Enter a table name
4. Data is automatically imported

**From JSON:**
1. Click **File → Import JSON**
2. Select your JSON file (must be array of objects)
3. Enter a table name
4. Data is automatically imported

### Exporting Data

**To CSV:**
1. Select the table to export
2. Click **File → Export Table (CSV)**
3. Choose save location
4. Opens in Excel/Google Sheets

**To JSON:**
1. Select the table to export
2. Click **File → Export Table (JSON)**
3. Choose save location
4. Can be used by other apps

### Backup & Restore

**Create Backup:**
1. Click **File → Backup Database**
2. Backup file created: `backup_YYYYMMDD_HHMMSS.db`
3. Save these files somewhere safe!

**Restore from Backup:**
1. Click **File → Restore Database**
2. Select a backup file
3. Confirm restoration
4. Database is restored

## 🔐 Security Features

### Setting a Password

1. Click **Tools → Set Password**
2. Enter a strong password
3. Password is required on next launch
4. **IMPORTANT:** Don't forget this password!

### Removing Password

1. Click **Tools → Set Password**
2. Leave password field empty
3. Click OK

### Best Practices

✅ Use a strong password (12+ characters)  
✅ Create regular backups  
✅ Keep backup on separate USB drive  
✅ Don't share your password  
✅ Test your backups regularly  

## 💡 Advanced Features

### SQL Queries

For advanced users, run custom SQL:

1. Click **Tools → SQL Query**
2. Enter your SQL command:
   ```sql
   SELECT * FROM customers WHERE age > 30
   ```
3. Click **Execute Query**

**Common SQL Commands:**
```sql
-- Get all records
SELECT * FROM table_name

-- Filter records
SELECT * FROM customers WHERE city = 'New York'

-- Update records
UPDATE customers SET status = 'active' WHERE id = 1

-- Delete records
DELETE FROM customers WHERE inactive = 'yes'

-- Count records
SELECT COUNT(*) FROM customers

-- Sort results
SELECT * FROM customers ORDER BY name
```

### Database Info

Click **Tools → Database Info** to see:
- Database location
- File size
- Number of tables
- Record counts
- Password status

## 🛠️ Troubleshooting

### Problem: "Python 3 is not installed"
**Solution:** Install Python 3 from [python.org](https://python.org)

### Problem: "Permission denied" on Mac/Linux
**Solution:** Make launcher executable:
```bash
chmod +x launch.sh
```

### Problem: Can't see tables/data
**Solution:** Click the 🔄 Refresh button

### Problem: Import failed
**Solution:** 
- CSV: Make sure first row has column names
- JSON: Must be an array of objects: `[{"name": "John"}, ...]`

### Problem: Forgot password
**Solution:** 
- Delete `config.json` file
- You'll lose password but keep data
- Or restore from backup made before password

### Problem: Database corrupted
**Solution:** 
- Restore from backup
- Or use SQLite recovery tools

## 📁 File Structure

```
portable_database/
├── portable_database.py   # Main application
├── launch.sh              # Mac/Linux launcher
├── launch.bat             # Windows launcher
├── portable_data.db       # Your database file
├── config.json            # Settings (password, etc.)
├── backup_*.db            # Backup files (if created)
└── README.md              # This file
```

## 🎓 Tips & Tricks

### 1. Organization
- Use meaningful table names (contacts, inventory, tasks)
- Keep related data in one table
- Use consistent naming (snake_case)

### 2. Data Entry
- Use TEXT for dates: "2025-11-12"
- Use INTEGER for counts, IDs
- Use REAL for prices, measurements
- Add a "notes" column for flexibility

### 3. Backups
- Backup before major changes
- Keep backups on different USB drives
- Test restoring from backup occasionally
- Name backups descriptively

### 4. Performance
- Search is fast even with 1000s of records
- For huge datasets (100K+ records), consider specialized database
- Regular backups help prevent issues

### 5. Portability
- Database files are ~10KB-10MB typically
- Entire system fits on any USB drive
- Works on any computer with Python 3
- No internet connection needed

## 🌟 Use Case Examples

### Small Business
- Customer database
- Inventory tracking
- Sales records
- Employee information

### Personal Use
- Password manager
- Recipe collection
- Book/movie library
- Contact manager
- Budget tracker

### Students
- Assignment tracker
- Research notes
- Contact list
- Study schedule

### Freelancers
- Client database
- Project tracker
- Invoice records
- Time tracking

### Events
- Guest list
- Vendor contacts
- Budget tracking
- Task lists

## 📊 Specifications

**Database Engine:** SQLite 3  
**GUI Framework:** Tkinter (included with Python)  
**File Size:** ~15KB (just the program)  
**Database Size:** Unlimited (limited by USB drive)  
**Platform Support:** Windows, Mac, Linux  
**Python Version:** 3.6+  
**Dependencies:** None (uses standard library)  

## 🔗 Resources

**Python Installation:**
- Windows: https://python.org/downloads
- Mac: Comes pre-installed or use `brew install python3`
- Linux: `sudo apt install python3`

**Learning SQL:**
- https://www.w3schools.com/sql
- https://sqlitetutorial.net

**SQLite Documentation:**
- https://sqlite.org/docs.html

## 📝 License

This software is provided as-is for personal and commercial use.
Feel free to modify and distribute.

## 💬 Tips for Success

1. **Start Simple** - Create one table, add a few records
2. **Experiment** - Try different column types
3. **Backup Often** - Better safe than sorry
4. **Use Search** - Faster than scrolling
5. **Learn SQL** - Unlock advanced features

## 🚀 Getting Started Checklist

- [ ] Copy program to USB drive
- [ ] Run launcher script
- [ ] Create first table
- [ ] Add some test data
- [ ] Try searching/filtering
- [ ] Export to CSV
- [ ] Create a backup
- [ ] Set a password (optional)
- [ ] Start using for real data!

---

**You now have a complete portable database system!**

Works on any computer, requires no installation, and keeps your data secure and portable.

Perfect for anyone who needs to manage data on the go! 🎉
