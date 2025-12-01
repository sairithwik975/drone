class Drone:
    def __init__(self,name,battery,altitude,speed):
        self.name=name
        self.battery=battery
        self.altitude=altitude
        self.speed=speed
    def show_status(self):
        print("Drone Name:", self.name)
        print("Battery level", self.battery,"%")
        print("Altitude:", self.altitude, "meters")
        print("Speed", self.speed, "km/h")
    def take_off(self):
        if self.battery<10:
            print("Battery too low to take off.")
            return 
        self.altitude=10
        self.speed=5
        self.battery-=5
        print("The drone", self.name, "has taken off.")
    def land(self):
        if self.altitude==0:
            print("The drone is already on the ground.")
            return
        self.altitude=0
        self.speed=0
        self.battery-=1
        print("The drone", self.name, "has landed.")
    def increase_altitude(self,meters):
        if self.battery<10:
            print("Battery too low to increase altitude.")
            return
        self.altitude+=meters
        self.battery-=0.5*meters
        print("The drone", self.name, "has increased altitude by", meters, "meters.")
d= Drone("phantom", 67,0,0)
d.take_off()
d.increase_altitude(20)
d.show_status()

