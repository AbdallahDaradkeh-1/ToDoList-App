import tkinter as tk

def adjust_height(event):
    # 'end-1c' gets all text excluding the final automatic newline character
    text_content = text_box.get("1.0", "end-1c")
    
    # Count the physical newline characters split by the user
    line_count = text_content.count("\n") + 1
    
    # Set boundaries so the widget doesn't get too small or too large
    min_height = 2
    max_height = 10
    
    # Calculate the new height dynamically
    new_height = max(min_height, min(line_count, max_height))
    
    # Apply the new height configuration
    text_box.config(height=new_height)

root = tk.Tk()
root.title("Dynamic Height Textbox")
root.geometry("400x300")

# Initialize the text box with a starting height
text_box = tk.Text(root, wrap="word", width=40, height=2)
text_box.pack(pady=20)

# Bind the function to trigger whenever a key is released
text_box.bind("<KeyRelease>", adjust_height)

root.mainloop()
