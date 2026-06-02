import tkinter as tk
from tkinter import ttk, messagebox

# Create the main window
root = tk.Tk()
root.title("Ruv Predictive Model")
root.geometry("480x320")

# Header
header = tk.Label(root, text="Ruv Predictive Model", font=("Arial", 18))
header.pack(pady=8)

# Controls frame
frame = tk.Frame(root)
frame.pack(padx=12, pady=6, fill=tk.BOTH, expand=True)

# Model selection
tk.Label(frame, text="Select model:").grid(row=0, column=0, sticky="w")
model_var = tk.StringVar(value="Model A")
model_combo = ttk.Combobox(frame, textvariable=model_var, values=["Model A", "Model B", "Model C"], state="readonly")
model_combo.grid(row=0, column=1, sticky="ew", padx=6, pady=2)

# Mode radio buttons
tk.Label(frame, text="Mode:").grid(row=1, column=0, sticky="w")
mode_var = tk.StringVar(value="fast")
mode_fast = tk.Radiobutton(frame, text="Fast", variable=mode_var, value="fast")
mode_acc = tk.Radiobutton(frame, text="Accurate", variable=mode_var, value="accurate")
mode_fast.grid(row=1, column=1, sticky="w")
mode_acc.grid(row=1, column=1, sticky="e")

# Feature toggles
tk.Label(frame, text="Options:").grid(row=2, column=0, sticky="w")
opt1_var = tk.BooleanVar(value=True)
opt2_var = tk.BooleanVar(value=False)
opt1 = tk.Checkbutton(frame, text="Enable pre-processing", variable=opt1_var)
opt2 = tk.Checkbutton(frame, text="Use ensemble", variable=opt2_var)
opt1.grid(row=2, column=1, sticky="w")
opt2.grid(row=3, column=1, sticky="w")

# Numeric parameter
tk.Label(frame, text="Parameter K:").grid(row=4, column=0, sticky="w")
param_var = tk.StringVar(value="5")
param_entry = tk.Entry(frame, textvariable=param_var, width=10)
param_entry.grid(row=4, column=1, sticky="w", padx=6, pady=2)

# Status label
status_var = tk.StringVar(value="Ready")
status = tk.Label(root, textvariable=status_var, anchor="w")
status.pack(fill=tk.X, padx=6, pady=(0,6))


def on_run():
	# Gather selections and show a summary
	model = model_var.get()
	mode = mode_var.get()
	opts = []
	if opt1_var.get():
		opts.append("pre-processing")
	if opt2_var.get():
		opts.append("ensemble")
	k = param_var.get()
	summary = f"Model: {model}\nMode: {mode}\nOptions: {', '.join(opts) or 'none'}\nK: {k}"
	status_var.set("Running...")
	root.update_idletasks()
	# In a real app you'd run the model here; we just show choices.
	messagebox.showinfo("Run configuration", summary)
	status_var.set("Ready")


# Run button
run_btn = tk.Button(root, text="Run", command=on_run)
run_btn.pack(pady=6)

# Make grid columns resize nicely
frame.columnconfigure(1, weight=1)

# Start GUI
root.mainloop()