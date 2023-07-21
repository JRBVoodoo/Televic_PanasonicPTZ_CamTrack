import tkinter as tk
import main
import threading


def initialize():
    main.initialize()
    main.startProgram()
    initialize_btn.config(state=tk.NORMAL)


def start_initialize_thread():
    # Disable the Initialize button during the initialization process
    initialize_btn.config(state=tk.DISABLED)
    # Start the initialization function in a separate thread
    init_thread = threading.Thread(target=initialize)
    init_thread.start()


def submit():
    # Get values from text boxes and checkboxes
    cam_values = {
        "Cam 1": {"ip": cam1_entry.get(), "enabled": cam1_var.get()},
        "Cam 2": {"ip": cam2_entry.get(), "enabled": cam2_var.get()},
        "Cam 3": {"ip": cam3_entry.get(), "enabled": cam3_var.get()},
        "Cam 4": {"ip": cam4_entry.get(), "enabled": cam4_var.get()},
        "Cam 5": {"ip": cam5_entry.get(), "enabled": cam5_var.get()},
        "Cam 6": {"ip": cam6_entry.get(), "enabled": cam6_var.get()},
    }

    # Add your code to use the entered values here
    for cam, values in cam_values.items():
        print(f"{cam} - IP: {values['ip']} - Enabled: {values['enabled']}")

# Create the main application window
root = tk.Tk()
root.title("Camera Configuration")

# Initialize button
initialize_btn = tk.Button(root, text="Initialize", command=start_initialize_thread)
initialize_btn.grid(row=0, column=0, columnspan=2, pady=5)

# Camera configurations
cam1_var = tk.StringVar()
cam1_var.set("enabled")
cam1_label = tk.Label(root, text="Camera IP 1:")
cam1_label.grid(row=1, column=0)
cam1_entry = tk.Entry(root)
cam1_entry.grid(row=1, column=1)
cam1_checkbox = tk.Checkbutton(root, text="Enabled", variable=cam1_var, onvalue="enabled", offvalue="disabled")
cam1_checkbox.grid(row=1, column=2)

cam2_var = tk.StringVar()
cam2_var.set("enabled")
cam2_label = tk.Label(root, text="Camera IP 2:")
cam2_label.grid(row=2, column=0)
cam2_entry = tk.Entry(root)
cam2_entry.grid(row=2, column=1)
cam2_checkbox = tk.Checkbutton(root, text="Enabled", variable=cam2_var, onvalue="enabled", offvalue="disabled")
cam2_checkbox.grid(row=2, column=2)

cam3_var = tk.StringVar()
cam3_var.set("enabled")
cam3_label = tk.Label(root, text="Camera IP 3:")
cam3_label.grid(row=3, column=0)
cam3_entry = tk.Entry(root)
cam3_entry.grid(row=3, column=1)
cam3_checkbox = tk.Checkbutton(root, text="Enabled", variable=cam3_var, onvalue="enabled", offvalue="disabled")
cam3_checkbox.grid(row=3, column=2)

cam4_var = tk.StringVar()
cam4_var.set("enabled")
cam4_label = tk.Label(root, text="Camera IP 4:")
cam4_label.grid(row=4, column=0)
cam4_entry = tk.Entry(root)
cam4_entry.grid(row=4, column=1)
cam4_checkbox = tk.Checkbutton(root, text="Enabled", variable=cam4_var, onvalue="enabled", offvalue="disabled")
cam4_checkbox.grid(row=4, column=2)

cam5_var = tk.StringVar()
cam5_var.set("enabled")
cam5_label = tk.Label(root, text="Camera IP 5:")
cam5_label.grid(row=5, column=0)
cam5_entry = tk.Entry(root)
cam5_entry.grid(row=5, column=1)
cam5_checkbox = tk.Checkbutton(root, text="Enabled", variable=cam5_var, onvalue="enabled", offvalue="disabled")
cam5_checkbox.grid(row=5, column=2)

cam6_var = tk.StringVar()
cam6_var.set("enabled")
cam6_label = tk.Label(root, text="Camera IP 6:")
cam6_label.grid(row=6, column=0)
cam6_entry = tk.Entry(root)
cam6_entry.grid(row=6, column=1)
cam6_checkbox = tk.Checkbutton(root, text="Enabled", variable=cam6_var, onvalue="enabled", offvalue="disabled")
cam6_checkbox.grid(row=6, column=2)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
