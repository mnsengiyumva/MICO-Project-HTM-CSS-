
import tkinter as tk

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x500")

label = tk.Label(root, text="Welcome to the Expense Tracker", font=("Arial",17))
label.pack(pady=20)

root.mainloop()