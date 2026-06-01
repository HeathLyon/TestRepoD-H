import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Yo Mama is the best")
root.geometry("300x150")

# Create a label
label = tk.Label(root, text="Yo Mama", font=("Arial", 24))
label.pack(expand=True)

# Run the application
root.mainloop()