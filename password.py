import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()

    # Criteria checks
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    number = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, bool(upper), bool(lower), bool(number), bool(special)])

    # Determine strength
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score == 3:
        strength = "Moderate"
        color = "orange"
    elif score == 4:
        strength = "Strong"
        color = "blue"
    else:
        strength = "Very Strong"
        color = "green"

    result_label.config(text=f"Strength: {strength}", fg=color)

    # Details popup
    details = f"""
Password Analysis:
--------------------------
Length (>=8):        {'✔' if length else '❌'}
Uppercase:           {'✔' if upper else '❌'}
Lowercase:           {'✔' if lower else '❌'}
Numbers:             {'✔' if number else '❌'}
Special Characters:  {'✔' if special else '❌'}
"""
    messagebox.showinfo("Password Details", details)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.config(bg="#1e1e1e")

title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 14))
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Strength", font=("Arial", 12, "bold"), command=check_password_strength, bg="#3e8ef7", fg="white")
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#1e1e1e")
result_label.pack(pady=10)

root.mainloop()
