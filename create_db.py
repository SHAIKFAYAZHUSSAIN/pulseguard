import sqlite3

conn = sqlite3.connect("donors.db")
cursor = conn.cursor()

# Remove old table
cursor.execute("DROP TABLE IF EXISTS donors")

# Create new table with phone_number column
cursor.execute("""
CREATE TABLE donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    blood_group TEXT NOT NULL,
    hemoglobin REAL NOT NULL,
    phone_number TEXT NOT NULL,
    location TEXT NOT NULL,
    available INTEGER NOT NULL
)
""")

# Add phone numbers for ALL donors
donors = [
    ("Rahul", "O+", 13.5, "9876543210", "Hyderabad", 1),
    ("Priya", "A+", 12.8, "9123456780", "Bangalore", 1),
    ("Arjun", "B+", 11.0, "9988776655", "Chennai", 1),
    ("Sneha", "O-", 14.2, "9001122334", "Mumbai", 1),
    ("Kiran", "AB+", 13.1, "8881234567", "Kolkata", 0),
    ("Meena", "A-", 13.8, "7776543210", "Delhi", 1),
    ("Vikram", "B-", 12.6, "9090909090", "Pune", 1),
    ("Anjali", "O+", 13.0, "9191919191", "Ahmedabad", 1),
    ("Ramesh", "O-", 15.1, "8181818181", "Jaipur", 1)
]

cursor.executemany("""
INSERT INTO donors (name, blood_group, hemoglobin, phone_number, location, available)
VALUES (?, ?, ?, ?, ?, ?)
""", donors)

conn.commit()
conn.close()

print("Donor database recreated successfully with phone numbers.")