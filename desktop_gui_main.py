from tkinter import *
from tkinter import ttk


import tkinter as tk


def show_message() -> None:
  message_label.config(text = "The button is connected to Python!")

window = tk.Tk()

window.title("My Application")
window.geometry("400x200")

message_label = tk.Label(window, text="Press the button")
message_label.pack(pady=30)
button = tk.Button(
  window,
  text="Click me",
  command=show_message,
)

button.pack()
window.mainloop()
