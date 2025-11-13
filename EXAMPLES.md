# 📝 USAGE EXAMPLES & TEMPLATES

## Ready-to-Use Table Templates

Copy these directly when creating new tables!

---

## 1️⃣ CONTACT MANAGER

**Table Name:** `contacts`

**Columns:**
```
name TEXT
email TEXT
phone TEXT
company TEXT
position TEXT
address TEXT
city TEXT
notes TEXT
created_date TEXT
```

**Sample Data:**
- Name: John Smith
- Email: john@techcorp.com
- Phone: 555-0123
- Company: Tech Corp
- Position: Sales Manager
- Address: 123 Main St
- City: New York
- Notes: Met at conference 2025
- Created_date: 2025-11-12

---

## 2️⃣ INVENTORY MANAGEMENT

**Table Name:** `inventory`

**Columns:**
```
item_name TEXT
sku TEXT
category TEXT
quantity INTEGER
price REAL
cost REAL
location TEXT
supplier TEXT
reorder_point INTEGER
last_updated TEXT
```

**Sample Data:**
- Item_name: Wireless Mouse
- SKU: WM-001
- Category: Electronics
- Quantity: 50
- Price: 29.99
- Cost: 15.00
- Location: Warehouse A, Shelf 12
- Supplier: Tech Supplies Inc
- Reorder_point: 10
- Last_updated: 2025-11-12

---

## 3️⃣ PASSWORD VAULT

**Table Name:** `passwords`

**⚠️ IMPORTANT: Set database password first!**  
Tools → Set Password

**Columns:**
```
service TEXT
username TEXT
password TEXT
email TEXT
url TEXT
category TEXT
notes TEXT
last_changed TEXT
```

**Sample Data:**
- Service: Gmail
- Username: myemail@gmail.com
- Password: SuperSecret123!
- Email: myemail@gmail.com
- URL: https://gmail.com
- Category: Email
- Notes: Main personal email
- Last_changed: 2025-11-12

---

## 4️⃣ PROJECT TRACKER

**Table Name:** `projects`

**Columns:**
```
project_name TEXT
client TEXT
status TEXT
priority TEXT
start_date TEXT
end_date TEXT
budget REAL
spent REAL
manager TEXT
notes TEXT
```

**Status Options:** Planning, In Progress, On Hold, Completed

**Sample Data:**
- Project_name: Website Redesign
- Client: ABC Company
- Status: In Progress
- Priority: High
- Start_date: 2025-10-01
- End_date: 2025-12-31
- Budget: 50000.00
- Spent: 15000.00
- Manager: Jane Doe
- Notes: Client wants modern design

---

## 5️⃣ EXPENSE TRACKER

**Table Name:** `expenses`

**Columns:**
```
date TEXT
category TEXT
description TEXT
amount REAL
payment_method TEXT
receipt_number TEXT
tax_deductible TEXT
notes TEXT
```

**Categories:** Food, Transport, Office, Travel, Equipment, Utilities

**Sample Data:**
- Date: 2025-11-12
- Category: Office
- Description: Paper supplies
- Amount: 45.99
- Payment_method: Credit Card
- Receipt_number: RCP-12345
- Tax_deductible: Yes
- Notes: Monthly office supplies

---

## 6️⃣ STUDENT RECORDS

**Table Name:** `students`

**Columns:**
```
student_id TEXT
first_name TEXT
last_name TEXT
email TEXT
phone TEXT
enrollment_date TEXT
grade_level TEXT
gpa REAL
status TEXT
notes TEXT
```

**Sample Data:**
- Student_id: S2025001
- First_name: Emily
- Last_name: Johnson
- Email: emily.j@school.edu
- Phone: 555-0199
- Enrollment_date: 2025-09-01
- Grade_level: 10th
- GPA: 3.85
- Status: Active
- Notes: Honor roll student

---

## 7️⃣ RECIPE COLLECTION

**Table Name:** `recipes`

**Columns:**
```
recipe_name TEXT
category TEXT
cuisine TEXT
prep_time INTEGER
cook_time INTEGER
servings INTEGER
difficulty TEXT
ingredients TEXT
instructions TEXT
notes TEXT
```

**Sample Data:**
- Recipe_name: Spaghetti Carbonara
- Category: Main Course
- Cuisine: Italian
- Prep_time: 10
- Cook_time: 20
- Servings: 4
- Difficulty: Medium
- Ingredients: Pasta, eggs, bacon, parmesan, black pepper
- Instructions: 1. Boil pasta 2. Fry bacon...
- Notes: Family favorite

---

## 8️⃣ EVENT PLANNING

**Table Name:** `event_guests`

**Columns:**
```
guest_name TEXT
email TEXT
phone TEXT
rsvp_status TEXT
meal_preference TEXT
plus_one TEXT
table_number INTEGER
notes TEXT
invitation_sent TEXT
```

**RSVP Status:** Pending, Accepted, Declined

**Sample Data:**
- Guest_name: Michael Brown
- Email: mbrown@email.com
- Phone: 555-0145
- RSVP_status: Accepted
- Meal_preference: Vegetarian
- Plus_one: Yes
- Table_number: 5
- Notes: Dietary restrictions noted
- Invitation_sent: 2025-10-15

---

## 9️⃣ BOOK LIBRARY

**Table Name:** `books`

**Columns:**
```
title TEXT
author TEXT
isbn TEXT
genre TEXT
pages INTEGER
rating REAL
status TEXT
date_started TEXT
date_finished TEXT
notes TEXT
```

**Status:** To Read, Reading, Completed

**Sample Data:**
- Title: The Great Gatsby
- Author: F. Scott Fitzgerald
- ISBN: 978-0-7432-7356-5
- Genre: Classic Fiction
- Pages: 180
- Rating: 4.5
- Status: Completed
- Date_started: 2025-10-01
- Date_finished: 2025-10-15
- Notes: Excellent prose

---

## 🔟 CUSTOMER DATABASE

**Table Name:** `customers`

**Columns:**
```
customer_id TEXT
company_name TEXT
contact_name TEXT
email TEXT
phone TEXT
address TEXT
city TEXT
state TEXT
zip TEXT
account_status TEXT
total_purchases REAL
last_purchase_date TEXT
notes TEXT
```

**Sample Data:**
- Customer_id: CUST-001
- Company_name: Acme Corporation
- Contact_name: Tom Wilson
- Email: tom@acme.com
- Phone: 555-0167
- Address: 456 Business Ave
- City: Chicago
- State: IL
- ZIP: 60601
- Account_status: Active
- Total_purchases: 15000.00
- Last_purchase_date: 2025-11-01
- Notes: Preferred customer, 10% discount

---

## 💡 Pro Tips for Each Use Case

### Contact Manager
- Export to CSV to sync with phone
- Use notes for last contact date
- Search by company to find all contacts

### Inventory
- Set reorder_point alerts
- Track cost vs price for profit
- Export monthly for accounting

### Password Vault
- **ALWAYS SET DATABASE PASSWORD**
- Include password change date
- Use strong passwords only
- Regular backups to separate USB

### Project Tracker
- Update spent weekly
- Use priority for task order
- Export to share with team

### Expense Tracker
- Separate tables for each year
- Mark tax_deductible for filing
- Monthly CSV export for taxes

### Student Records
- One table per class/semester
- Link to assignments table
- Export for report cards

### Recipe Collection
- Use JSON export to share
- Take photos, note in description
- Scale servings as needed

### Event Planning
- Track RSVPs in real-time
- Print guest list from CSV
- Notes for seating preferences

### Book Library
- Rating system 1-5
- Track reading progress
- Export reading lists

### Customer Database
- Link to sales table
- Track purchase history
- Regular backup before changes

---

## 🎯 Advanced Multi-Table Examples

### Complete CRM System

**Table 1: Customers**
```
customer_id TEXT (e.g., CUST-001)
company_name TEXT
contact_name TEXT
email TEXT
phone TEXT
```

**Table 2: Sales**
```
sale_id TEXT (e.g., SALE-001)
customer_id TEXT (links to customers)
sale_date TEXT
amount REAL
status TEXT
```

**Table 3: Follow_ups**
```
followup_id TEXT
customer_id TEXT (links to customers)
date TEXT
type TEXT
notes TEXT
```

### School Management

**Table 1: Students**
**Table 2: Classes**
**Table 3: Grades**
**Table 4: Attendance**

Link them using student_id!

---

## 📊 Import/Export Workflows

### Excel → Database
1. Save Excel as CSV
2. File → Import CSV
3. Name your table
4. Edit in database
5. Export back to CSV when done

### Database → Shared Document
1. Export table to CSV
2. Upload to Google Sheets
3. Share with team
4. Re-import updates

### Backup Strategy
1. Weekly: File → Backup Database
2. Save to different USB
3. Monthly: Export all tables to CSV
4. Keep CSV copies in cloud

---

## 🔍 Search Examples

**Find by name:**
Type: "john" (searches all columns)

**Find by date:**
Type: "2025-11" (finds all Nov 2025)

**Find by category:**
Type: "urgent" or "important"

**Find by number:**
Type: "555" (finds all with 555 in any field)

---

## 💾 Best Practices

1. **Consistent Naming**
   - Use snake_case: `customer_name`
   - Not camelCase: `customerName`

2. **Date Format**
   - Always: YYYY-MM-DD (2025-11-12)
   - Sorts correctly
   - Universal format

3. **Required Fields**
   - Name/ID field in every table
   - Date created field
   - Notes field for flexibility

4. **Regular Maintenance**
   - Weekly backups
   - Monthly exports (CSV)
   - Quarterly cleanup (delete old data)

5. **Security**
   - Password protect sensitive tables
   - Regular backups to separate location
   - Don't share database file directly

---

**Ready to use these templates?**

Just copy the column definitions when creating new tables!

All templates tested and ready to go! 🚀
