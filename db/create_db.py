import sqlite3

# Connect to the database (this will create the .db file if it doesn't exist)
conn = sqlite3.connect('voorraad.db')
cursor = conn.cursor()

# Create Snacks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Snacks (
    unique_id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    unit_price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date TEXT NOT NULL
);
''')

# Create Drinks table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Drinks (
    unique_id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    unit_price_per_liter REAL NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date TEXT NOT NULL
);
''')

# Insert sample data into Snacks table
cursor.execute('''INSERT INTO Snacks (unique_id, name, unit_price, quantity, expiration_date) VALUES 
('SN-0001', 'Chips', 1.50, 100, '12-12-2024'),
('SN-0002', 'Popcorn', 1.20, 80, '01-11-2024'),
('SN-0003', 'Cookies', 2.00, 50, '10-01-2025'),
('SN-0004', 'Pretzels', 1.30, 120, '05-05-2024'),
('SN-0005', 'Candy Bar', 1.10, 70, '20-06-2024'),
('SN-0006', 'Nuts', 2.50, 30, '15-03-2025'),
('SN-0007', 'Chocolate', 2.80, 40, '22-07-2024'),
('SN-0008', 'Gum', 0.50, 200, '30-09-2024'),
('SN-0009', 'Crackers', 1.70, 90, '12-08-2024'),
('SN-0010', 'Granola Bar', 1.90, 60, '17-10-2024'),
('SN-0011', 'Beef Jerky', 3.50, 25, '23-04-2025'),
('SN-0012', 'Trail Mix', 2.20, 35, '09-02-2025'),
('SN-0013', 'Rice Cakes', 1.40, 85, '31-01-2025'),
('SN-0014', 'Fruit Snacks', 1.30, 95, '13-06-2024'),
('SN-0015', 'Pita Chips', 2.10, 50, '26-07-2024'),
('SN-0016', 'Veggie Chips', 2.30, 45, '19-08-2024'),
('SN-0017', 'Cheese Puffs', 1.80, 110, '25-09-2024'),
('SN-0018', 'Yogurt Bites', 2.40, 35, '12-10-2024'),
('SN-0019', 'Energy Bites', 2.60, 40, '18-11-2024'),
('SN-0020', 'Peanut Butter Cups', 3.00, 30, '28-12-2024');
''')

# Insert sample data into Drinks table
cursor.execute('''INSERT INTO Drinks (unique_id, name, unit_price_per_liter, quantity, expiration_date) VALUES 
('AB-0001', 'Milk', 2.30, 20, '12-12-2024'),
('AB-0002', 'Orange Juice', 3.20, 15, '01-01-2025'),
('AB-0003', 'Apple Juice', 3.10, 18, '10-02-2025'),
('AB-0004', 'Sparkling Water', 1.50, 25, '05-03-2024'),
('AB-0005', 'Soda', 1.20, 50, '20-06-2024'),
('AB-0006', 'Iced Tea', 1.80, 30, '15-07-2024'),
('AB-0007', 'Lemonade', 2.00, 22, '22-08-2024'),
('AB-0008', 'Energy Drink', 2.50, 18, '30-09-2024'),
('AB-0009', 'Smoothie', 3.00, 10, '12-10-2024'),
('AB-0010', 'Coffee', 2.70, 40, '17-11-2024'),
('AB-0011', 'Tea', 2.40, 35, '23-12-2024'),
('AB-0012', 'Hot Chocolate', 2.90, 25, '09-01-2025'),
('AB-0013', 'Protein Shake', 3.50, 15, '31-01-2025'),
('AB-0014', 'Almond Milk', 2.80, 20, '13-02-2025'),
('AB-0015', 'Soy Milk', 2.60, 25, '26-03-2024'),
('AB-0016', 'Coconut Water', 2.50, 18, '19-04-2025'),
('AB-0017', 'Vegetable Juice', 3.30, 12, '25-05-2024'),
('AB-0018', 'Cranberry Juice', 3.20, 20, '12-06-2024'),
('AB-0019', 'Grape Juice', 3.10, 16, '18-07-2024'),
('AB-0020', 'Mineral Water', 1.80, 30, '28-08-2024');
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'voorraad.db' created and data inserted.")
