import sqlite3

conn = sqlite3.connect("donors.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    blood_group TEXT,
    hemoglobin REAL,
    available INTEGER
)
""")

# Insert dummy donors
donors = [
    ("Rahul", "O+", 13.5, 1),
    ("Priya", "A+", 12.8, 1),
    ("Arjun", "B+", 11.0, 1),
    ("Sneha", "O-", 14.2, 1),
    ("Kiran", "AB+", 13.1, 0),
    ("Meena", "A-", 13.8, 1),
    ("Vikram", "B-", 12.6, 1),
    ("Anjali", "O+", 13.0, 1),
    ("Ramesh", "O-", 15.1, 1)
]

cursor.executemany("""
INSERT INTO donors (name, blood_group, hemoglobin, available)
VALUES (?, ?, ?, ?)
""", donors)

conn.commit()
conn.close()

print("Donor database created successfully.")