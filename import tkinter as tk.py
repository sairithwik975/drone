import tkinter as tk
from tkinter import scrolledtext
import random

# -----------------------------------------------------------
# YOUR EXISTING DRONE CLASS (Slightly modified for GUI)
# -----------------------------------------------------------
class Drone:
    def __init__(self, name, battery, altitude, speed):
        self.name = name
        self.battery = battery
        self.altitude = altitude
        self.speed = speed
        # GPS Coordinates
        self.x = 0
        self.y = 0

    def take_off(self):
        if self.battery < 10:
            return "Battery too low to take off."
        self.altitude = 10
        self.speed = 5
        self.battery -= 5
        return f"Drone {self.name} has taken off."

    def land(self):
        if self.altitude == 0:
            return "Drone is already on the ground."
        self.altitude = 0
        self.speed = 0
        self.battery -= 2
        return f"Drone {self.name} has landed."

    def increase_altitude(self, meters):
        if self.battery < 10:
            return "Battery too low."
        self.altitude += meters
        self.battery -= 0.5 * meters
        return f"Altitude increased by {meters}m."

    def decrease_altitude(self, meters):
        if self.altitude == 0:
            return "Drone is on ground."
        actual_change = min(self.altitude, meters)
        self.altitude -= actual_change
        self.battery -= 0.2 * actual_change
        return f"Altitude decreased by {actual_change}m."

    def move(self, direction, meters):
        if self.altitude == 0:
            return "Must be airborne to move."
        
        if direction == "north":
            self.y += meters
        elif direction == "south":
            self.y -= meters
        elif direction == "east":
            self.x += meters
        elif direction == "west":
            self.x -= meters
            
        self.battery -= 0.1 * meters
        return f"Moved {direction} by {meters}m. Pos: ({self.x}, {self.y})"

# -----------------------------------------------------------
# THE GUI CLASS (The Control Panel)
# -----------------------------------------------------------
class DroneControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Control Station")
        self.root.geometry("600x500")

        # Initialize the Drone Logic
        self.drone = Drone("Phantom", 100, 0, 0)

        # --- LEFT SIDE: STATUS DISPLAY ---
        self.status_frame = tk.LabelFrame(root, text="Live Telemetry", padx=10, pady=10)
        self.status_frame.place(x=20, y=20, width=250, height=200)

        self.lbl_battery = tk.Label(self.status_frame, text="Battery: 100%", font=("Arial", 12))
        self.lbl_battery.pack(anchor="w")
        
        self.lbl_altitude = tk.Label(self.status_frame, text="Altitude: 0m", font=("Arial", 12))
        self.lbl_altitude.pack(anchor="w")

        self.lbl_speed = tk.Label(self.status_frame, text="Speed: 0 km/h", font=("Arial", 12))
        self.lbl_speed.pack(anchor="w")

        self.lbl_pos = tk.Label(self.status_frame, text="Pos: (0, 0)", font=("Arial", 12))
        self.lbl_pos.pack(anchor="w")

        # --- RIGHT SIDE: CONTROLS ---
        self.control_frame = tk.LabelFrame(root, text="Flight Controls", padx=10, pady=10)
        self.control_frame.place(x=290, y=20, width=280, height=250)

        # Input box for values
        tk.Label(self.control_frame, text="Value (meters/speed):").grid(row=0, column=0, columnspan=2)
        self.input_value = tk.Entry(self.control_frame)
        self.input_value.insert(0, "10") # Default value
        self.input_value.grid(row=1, column=0, columnspan=2, pady=5)

        # Buttons
        tk.Button(self.control_frame, text="Take Off", bg="green", fg="white", command=self.action_takeoff).grid(row=2, column=0, sticky="ew", padx=2, pady=2)
        tk.Button(self.control_frame, text="Land", bg="red", fg="white", command=self.action_land).grid(row=2, column=1, sticky="ew", padx=2, pady=2)

        tk.Button(self.control_frame, text="Up", command=lambda: self.action_altitude("up")).grid(row=3, column=0, sticky="ew", padx=2, pady=2)
        tk.Button(self.control_frame, text="Down", command=lambda: self.action_altitude("down")).grid(row=3, column=1, sticky="ew", padx=2, pady=2)

        # Direction Pad
        tk.Button(self.control_frame, text="North", command=lambda: self.action_move("north")).grid(row=4, column=0, columnspan=2, sticky="ew", padx=2, pady=2)
        tk.Button(self.control_frame, text="West", command=lambda: self.action_move("west")).grid(row=5, column=0, sticky="ew", padx=2, pady=2)
        tk.Button(self.control_frame, text="East", command=lambda: self.action_move("east")).grid(row=5, column=1, sticky="ew", padx=2, pady=2)
        tk.Button(self.control_frame, text="South", command=lambda: self.action_move("south")).grid(row=6, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

        # --- BOTTOM: LOGS ---
        tk.Label(root, text="Mission Logs:").place(x=20, y=230)
        self.log_area = scrolledtext.ScrolledText(root, width=68, height=10)
        self.log_area.place(x=20, y=250)

    # --- HELPER FUNCTIONS ---
    def get_value(self):
        """Gets the number from the input box, defaults to 0 if invalid"""
        try:
            return int(self.input_value.get())
        except ValueError:
            return 0

    def update_gui(self, message):
        """Refreshes the labels and adds to the log box"""
        # Update Labels
        self.lbl_battery.config(text=f"Battery: {self.drone.battery:.1f}%")
        self.lbl_altitude.config(text=f"Altitude: {self.drone.altitude}m")
        self.lbl_speed.config(text=f"Speed: {self.drone.speed} km/h")
        self.lbl_pos.config(text=f"Pos: ({self.drone.x}, {self.drone.y})")
        
        # Update Log
        self.log_area.insert(tk.END, f"> {message}\n")
        self.log_area.see(tk.END) # Auto scroll to bottom

    # --- BUTTON ACTIONS ---
    def action_takeoff(self):
        msg = self.drone.take_off()
        self.update_gui(msg)

    def action_land(self):
        msg = self.drone.land()
        self.update_gui(msg)

    def action_altitude(self, direction):
        val = self.get_value()
        if direction == "up":
            msg = self.drone.increase_altitude(val)
        else:
            msg = self.drone.decrease_altitude(val)
        self.update_gui(msg)

    def action_move(self, direction):
        val = self.get_value()
        msg = self.drone.move(direction, val)
        self.update_gui(msg)

# -----------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = DroneControlPanel(root)
    root.mainloop()