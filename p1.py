import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
# CSV file to store the data
file_name = "product_sales.csv"
# Try to load existing data, else create new
try:
    data = pd.read_csv(file_name)
except FileNotFoundError:
    data = pd.DataFrame(columns=["Product", "Sales"])
    data.to_csv(file_name, index=False)
# Function to add data from GUI
def add_data():
    product = product_entry.get()
    sales = sales_entry.get()
    if not product or not sales:
        messagebox.showerror("Error", "Please enter both Product and Sales")
        return
    try:
        sales = int(sales)
    except ValueError:
        messagebox.showerror("Error", "Sales must be a number")
        return
    global data
    new_row = pd.DataFrame({"Product": [product], "Sales": [sales]})
    data = pd.concat([data, new_row], ignore_index=True)
    data.to_csv(file_name, index=False)
    messagebox.showinfo("Success", f"Added {product} with sales {sales}")
    product_entry.delete(0, tk.END)
    sales_entry.delete(0, tk.END)
# Function to plot bar chart
def plot_chart():
    if data.empty:
        messagebox.showerror("Error", "No data to plot")
        return
    plt.figure(figsize=(8,5))
    plt.bar(data["Product"], data["Sales"], color='skyblue', label="Sales")
    plt.title("Product Sales Chart")
    plt.xlabel("Products")
    plt.ylabel("Sales")
    plt.legend()
    plt.show()
# GUI window
root = tk.Tk()
root.title("Product Sales Entry")
tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=5)
product_entry = tk.Entry(root)
product_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Sales:").grid(row=1, column=0, padx=10, pady=5)
sales_entry = tk.Entry(root)
sales_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Add Data", command=add_data).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Plot Bar Chart", command=plot_chart).grid(row=3, column=0, columnspan=2, pady=10)
root.mainloop()