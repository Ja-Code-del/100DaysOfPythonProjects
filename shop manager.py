import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
from ttkthemes import ThemedTk

# Database setup
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    quantity INTEGER,
    cost_price REAL,
    selling_price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    type TEXT,
    date TEXT,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
''')

conn.commit()


# Functions
def add_product():
    name = entry_name.get()
    quantity = int(entry_quantity.get())
    cost_price = float(entry_cost_price.get())
    selling_price = float(entry_selling_price.get())

    cursor.execute('''
    INSERT INTO products (name, quantity, cost_price, selling_price)
    VALUES (?, ?, ?, ?)
    ''', (name, quantity, cost_price, selling_price))
    conn.commit()
    messagebox.showinfo("Success", "Product added successfully!")
    clear_entries()


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_cost_price.delete(0, tk.END)
    entry_selling_price.delete(0, tk.END)


def record_transaction(product_id, quantity, type):
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT INTO transactions (product_id, quantity, type, date)
    VALUES (?, ?, ?, ?)
    ''', (product_id, quantity, type, date))
    conn.commit()


def add_stock():
    product_id = int(entry_product_id.get())
    quantity = int(entry_transaction_quantity.get())

    cursor.execute('''
    UPDATE products
    SET quantity = quantity + ?
    WHERE id = ?
    ''', (quantity, product_id))
    conn.commit()
    record_transaction(product_id, quantity, 'in')
    messagebox.showinfo("Success", "Stock added successfully!")
    clear_transaction_entries()


def remove_stock():
    product_id = int(entry_product_id.get())
    quantity = int(entry_transaction_quantity.get())

    cursor.execute('''
    UPDATE products
    SET quantity = quantity - ?
    WHERE id = ?
    ''', (quantity, product_id))
    conn.commit()
    record_transaction(product_id, quantity, 'out')
    messagebox.showinfo("Success", "Stock removed successfully!")
    clear_transaction_entries()


def clear_transaction_entries():
    entry_product_id.delete(0, tk.END)
    entry_transaction_quantity.delete(0, tk.END)


def record_sale():
    product_id = int(entry_sale_product_id.get())
    quantity = int(entry_sale_quantity.get())

    cursor.execute('''
    UPDATE products
    SET quantity = quantity - ?
    WHERE id = ?
    ''', (quantity, product_id))
    conn.commit()
    record_transaction(product_id, quantity, 'sale')
    messagebox.showinfo("Success", "Sale recorded successfully!")
    clear_sale_entries()


def clear_sale_entries():
    entry_sale_product_id.delete(0, tk.END)
    entry_sale_quantity.delete(0, tk.END)


def calculate_profit():
    cursor.execute('''
    SELECT p.name, SUM(t.quantity * (p.selling_price - p.cost_price)) as profit
    FROM transactions t
    JOIN products p ON t.product_id = p.id
    WHERE t.type = 'sale'
    GROUP BY p.id
    ''')
    profits = cursor.fetchall()

    report_text.delete('1.0', tk.END)
    total_profit = 0
    for product, profit in profits:
        report_text.insert(tk.END, f"Product: {product}, Profit: ${profit:.2f}\n")
        total_profit += profit
    report_text.insert(tk.END, f"\nTotal Profit: ${total_profit:.2f}")


# GUI setup
root = ThemedTk(theme="breeze")
root.title("Store Management System")

style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TEntry', font=('Helvetica', 12))

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Frame for adding products
frame_add_product = ttk.Frame(notebook)
frame_add_product.pack(fill='both', expand=True)

label_name = ttk.Label(frame_add_product, text="Product Name:")
label_name.pack(pady=5)
entry_name = ttk.Entry(frame_add_product)
entry_name.pack(pady=5)

label_quantity = ttk.Label(frame_add_product, text="Quantity:")
label_quantity.pack(pady=5)
entry_quantity = ttk.Entry(frame_add_product)
entry_quantity.pack(pady=5)

label_cost_price = ttk.Label(frame_add_product, text="Cost Price:")
label_cost_price.pack(pady=5)
entry_cost_price = ttk.Entry(frame_add_product)
entry_cost_price.pack(pady=5)

label_selling_price = ttk.Label(frame_add_product, text="Selling Price:")
label_selling_price.pack(pady=5)
entry_selling_price = ttk.Entry(frame_add_product)
entry_selling_price.pack(pady=5)

button_add_product = ttk.Button(frame_add_product, text="Add Product", command=add_product)
button_add_product.pack(pady=20)

# Frame for managing stock
frame_manage_stock = ttk.Frame(notebook)
frame_manage_stock.pack(fill='both', expand=True)

label_product_id = ttk.Label(frame_manage_stock, text="Product ID:")
label_product_id.pack(pady=5)
entry_product_id = ttk.Entry(frame_manage_stock)
entry_product_id.pack(pady=5)

label_transaction_quantity = ttk.Label(frame_manage_stock, text="Quantity:")
label_transaction_quantity.pack(pady=5)
entry_transaction_quantity = ttk.Entry(frame_manage_stock)
entry_transaction_quantity.pack(pady=5)

button_add_stock = ttk.Button(frame_manage_stock, text="Add Stock", command=add_stock)
button_add_stock.pack(pady=5)

button_remove_stock = ttk.Button(frame_manage_stock, text="Remove Stock", command=remove_stock)
button_remove_stock.pack(pady=5)

# Frame for recording sales
frame_sales = ttk.Frame(notebook)
frame_sales.pack(fill='both', expand=True)

label_sale_product_id = ttk.Label(frame_sales, text="Product ID:")
label_sale_product_id.pack(pady=5)
entry_sale_product_id = ttk.Entry(frame_sales)
entry_sale_product_id.pack(pady=5)

label_sale_quantity = ttk.Label(frame_sales, text="Quantity:")
label_sale_quantity.pack(pady=5)
entry_sale_quantity = ttk.Entry(frame_sales)
entry_sale_quantity.pack(pady=5)

button_record_sale = ttk.Button(frame_sales, text="Record Sale", command=record_sale)
button_record_sale.pack(pady=20)

# Frame for generating reports
frame_report = ttk.Frame(notebook)
frame_report.pack(fill='both', expand=True)

button_generate_report = ttk.Button(frame_report, text="Generate Profit Report", command=calculate_profit)
button_generate_report.pack(pady=20)

report_text = tk.Text(frame_report, height=15, width=50)
report_text.pack(pady=10)

notebook.add(frame_add_product, text='Add Product')
notebook.add(frame_manage_stock, text='Manage Stock')
notebook.add(frame_sales, text='Sales')
notebook.add(frame_report, text='Reports')

root.mainloop()

# Close the database connection when the application closes
conn.close()
