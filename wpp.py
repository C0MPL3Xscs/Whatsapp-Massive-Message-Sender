import tkinter as tk
from tkinter import messagebox
import time
import webbrowser as web
from urllib.parse import quote
import pyautogui as pg
from pywhatkit.core import core

def send_messages():
    phone = phone_entry.get()
    message = message_entry.get()
    x = int(x_entry.get())

    for i in range(x):

        if i == 0: 
            web.open(f"https://web.whatsapp.com/send?phone={phone}&text={quote(message)}")
            time.sleep(5)
        else: pg.typewrite(message)
        pg.click(core.WIDTH / 2, core.HEIGHT / 2)
        pg.press("enter")
        if i == x-1:
            core.close_tab(wait_time=3)
    messagebox.showinfo("Success", "Messages sent successfully!")

root = tk.Tk()
root.title("WhatsApp Message Sender")

phone_label = tk.Label(root, text="Enter Phone Number:")
phone_label.grid(row=0, column=0)

phone_entry = tk.Entry(root)
phone_entry.grid(row=0, column=1)

message_label = tk.Label(root, text="Enter Message:")
message_label.grid(row=1, column=0)

message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1)

x_label = tk.Label(root, text="Enter number of messages:")
x_label.grid(row=2, column=0)

x_entry = tk.Entry(root)
x_entry.grid(row=2, column=1)

send_button = tk.Button(root, text="Send", command=send_messages)
send_button.grid(row=3, column=1)

root.mainloop()
