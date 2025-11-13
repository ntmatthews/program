# 🚀 QUICK START GUIDE

## 5-Minute Setup

### Step 1: Copy to USB Drive
```
1. Copy this entire folder to your USB drive
2. That's it! The database is now portable
```

### Step 2: Launch the Application

**On Windows:**
- Double-click `launch.bat`

**On Mac/Linux:**
- Double-click `launch.sh`
- (If it doesn't work, open Terminal and run: `chmod +x launch.sh`)

**Alternative:**
- Open Terminal/Command Prompt
- Navigate to this folder
- Run: `python3 portable_database.py`

### Step 3: Create Your First Table (30 seconds)

1. Click **File → New Table**
2. Enter name: `contacts`
3. Paste these columns:
   ```
   name TEXT
   email TEXT
   phone TEXT
   company TEXT
   ```
4. Click **Create Table**

### Step 4: Add Your First Record (30 seconds)

1. Select `contacts` from left panel
2. Click **➕ Add Record**
3. Fill in the fields:
   - Name: John Doe
   - Email: john@example.com
   - Phone: 555-1234
   - Company: Tech Corp
4. Click **Save Record**

### Step 5: Try These Features

**Search:** Type in the search box to filter records  
**Edit:** Select a record → Click ✏️ Edit  
**Delete:** Select a record → Click 🗑️ Delete  
**Export:** File → Export Table (CSV) - opens in Excel!  
**Backup:** File → Backup Database (do this regularly!)  

## 🎯 Ready-Made Table Templates

### Contact Manager
```
name TEXT
email TEXT
phone TEXT
company TEXT
address TEXT
notes TEXT
```

### Inventory System
```
item_name TEXT
sku TEXT
quantity INTEGER
price REAL
location TEXT
supplier TEXT
```

### Password Vault (with password protection!)
```
service TEXT
username TEXT
password TEXT
url TEXT
category TEXT
notes TEXT
```

### Project Tracker
```
project_name TEXT
client TEXT
status TEXT
start_date TEXT
end_date TEXT
budget REAL
notes TEXT
```

### Expense Tracker
```
date TEXT
category TEXT
description TEXT
amount REAL
payment_method TEXT
notes TEXT
```

## 💡 Pro Tips

1. **Always Create Backups**
   - File → Backup Database
   - Save backup to different USB or cloud

2. **Protect Sensitive Data**
   - Tools → Set Password
   - Now password required to open

3. **Import Existing Data**
   - File → Import CSV (from Excel)
   - File → Import JSON (from other apps)

4. **Use Search Effectively**
   - Searches ALL columns
   - Great for quick lookups

5. **Export for Sharing**
   - Export to CSV → Share via email
   - Export to JSON → Use in other apps

## 🎓 Video Tutorials (Text Version)

### Tutorial 1: Basic CRUD
```
1. Create table → File → New Table
2. Add data → Select table → ➕ Add Record
3. Edit data → Select record → ✏️ Edit Record
4. Delete data → Select record → 🗑️ Delete Record
```

### Tutorial 2: Import/Export
```
1. Export table → File → Export (CSV/JSON)
2. Edit in Excel
3. Import back → File → Import CSV
4. Changes applied!
```

### Tutorial 3: Backup Strategy
```
1. Create backup → File → Backup Database
2. Copy backup to cloud (Dropbox, Google Drive)
3. Test restore occasionally
4. Sleep well knowing data is safe!
```

## ❓ FAQ

**Q: Do I need internet?**  
A: No! 100% offline.

**Q: Can I use on multiple computers?**  
A: Yes! Just plug in USB and run.

**Q: What if I forget my password?**  
A: Delete `config.json` to reset (data stays safe).

**Q: How much data can I store?**  
A: Limited only by your USB drive size. Database handles millions of records.

**Q: Can I use with Excel?**  
A: Yes! Export to CSV, edit in Excel, import back.

**Q: Is it safe?**  
A: Your data stays on your USB. Set password for extra security.

**Q: Do I need Python installed?**  
A: Yes, Python 3.6+ required. Download from python.org

## 🆘 Need Help?

1. **Read the full README.md** - Detailed documentation
2. **Check troubleshooting section** - Common solutions
3. **Look at examples** - See how others use it

## ✅ Quick Checklist

- [ ] Program copied to USB drive
- [ ] Launcher works
- [ ] First table created
- [ ] First record added
- [ ] Backup created
- [ ] Password set (if needed)
- [ ] Ready to use!

---

**That's it! You're ready to go!** 🎉

Your complete portable database system is ready to use on any computer.
