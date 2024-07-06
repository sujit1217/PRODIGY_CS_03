import re
from tkinter import Tk, Entry, Label, Button, StringVar

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    # Lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    # Numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
    
    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")
    
    return strength, feedback

def assess_password():
    password = password_var.get()
    strength, feedback = check_password_strength(password)
    strength_label.config(text=f"Password Strength: {strength}/5")
    feedback_label.config(text="\n".join(feedback))

root = Tk()
root.title("Password Strength Checker")

password_var = StringVar()

Label(root, text="Enter your password:").pack()
Entry(root, textvariable=password_var, show='*').pack()

Button(root, text="Check Strength", command=assess_password).pack()

strength_label = Label(root, text="Password Strength: ")
strength_label.pack()

feedback_label = Label(root, text="", wraplength=300)
feedback_label.pack()

root.mainloop()
