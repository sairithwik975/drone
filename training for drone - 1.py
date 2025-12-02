import random
class Drone:
    def __init__(self,name,battery,altitude,speed):
        self.name=name
        self.battery=battery
        self.altitude=altitude
        self.speed=speed
        self.logs=[]

        self.x=0
        self.y=0

    def show_status(self):
        print("Drone Name:", self.name)
        print("Battery level", self.battery,"%")
        print("Altitude:", self.altitude, "meters")
        print("Speed", self.speed, "km/h")
        print("Position:",(self.x,self.y))
    def take_off(self):
        if self.battery<10:
            print("Battery too low to take off.")
            return 
        self.altitude=10
        self.speed=5
        self.battery-=5
        print("The drone", self.name, "has taken off.")
        self.add_log("Take off initiated.")
    def land(self):
        if self.altitude==0:
            print("The drone is already on the ground.")
            return
        self.altitude=0
        self.speed=0
        self.battery-=1
        print("The drone", self.name, "has landed.")
        self.add_log("Landing initiated.")
    def increase_altitude(self,meters):
        if self.battery<10:
            print("Battery too low to increase altitude.")
            return
        self.altitude+=meters
        self.battery-=0.5*meters
        print("The drone", self.name, "has increased altitude by", meters, "meters.")
        self.add_log("Increased altitude by "+str(meters)+" meters.")   
    def decrease_altitude(self,meters):
        if self.altitude==0:
            print("The drone is already on ground")
            return
        if meters>self.altitude:
            print("cannot decrease altitude below0")
            return
        self.altitude-=meters
        self.battery-=0.5*meters
        print("The drone", self.name, "has decreased altitude by", meters, "meters.")
        self.add_log("Decreased altitude by "+str(meters)+" meters.")
    def increase_speed(self,kmph):
        if self.battery<5:
            print("bettery is too low to increase speed.")
            return
        self.speed+=kmph
        self.battery-=0.2*kmph
        print("the drone", self.name, "has increased speed by", kmph, "km/h.")
        self.add_log("Increased speed by "+str(kmph)+" km/h.")
    def decrease_speed(self,kmph):
        if self.speed==0:
            print("the drone is already stationary.")
            return
        if kmph>self.speed:
            print("cannot decrease speed below 0.")
            return
        self.speed-=kmph
        self.battery-=0.2*kmph
        print("the drone", self.name, "has decreased speed by", kmph, "km/h.")
        self.add_log("Decreased speed by "+str(kmph)+" km/h.")  
    def emergency_stop(self):
        print("⚠️ EMERGENCY STOP ACTIVATED! ⚠️", self.name)
        self.speed=0
        self.altitude=0
        self.battery-=10
        print("The drone", self.name, "has performed an emergency stop.")    
        self.add_log("Emergency stop activated.")
    def battery_drain(self):
        if self.altitude>0:
            if self.speed>0:
                self.battery-=0.5
            else:
                self.battery-=0.2
        if self.battery<0:
            self.battery=0
        self.auto_return_home()
        self.add_log("Battery drained. Current level: "+str(self.battery)+"%.") 
    def auto_return_home(self):
        if self.battery<=15:
            print("The drone", self.name, "is returning home.")
            self.altitude=0
            self.speed=0
            self.battery-=3 
            print("The drone", self.name, "has landed at home.")
            self.add_log("Auto return home initiated due to low battery or altitude.")
    def move_north(self,meters):
        if self.altitude==0:
            print("the drone must be airborne to move.")
            return
        self.y+=meters
        self.battery-=0.1*meters
        print("the drone", self.name, "has moved north by", meters, "meters")
        self.add_log("Moved north by "+str(meters)+" meters.")
    def move_south(self,meters):
        if self.altitude==0:
            print("the drone must be airborne to move.")
            return
        self.y-=meters
        self.battery-=0.1*meters
        print("the drone", self.name, "has moved south by", meters, "meters")
        self.add_log("Moved south by "+str(meters)+" meters.")
    def move_east(self,meters):
        if self.altitude==0:
            print("the drone must be airborne to move.")
            return
        self.x+=meters
        self.battery-=0.1*meters
        print("the drone", self.name, "has moved east by", meters, "meters")
        self.add_log("Moved east by "+str(meters)+" meters.")
    def move_west(self,meters):
        if self.altitude==0:
            print("the drone must be airborne to move.")
            return
        self.x-=meters
        self.battery-=0.1*meters
        print("the drone", self.name, "has moved west by", meters, "meters")
        self.add_log("Moved west by "+str(meters)+" meters.")
    def altitude_sensor(self):
        print("Current altitude of drone", self.name, "is", self.altitude, "meters.")
        self.add_log("Altitude reading: "+str(self.altitude)+" meters.")
    def battery_sensor(self):
        print("Current battery level of drone", self.name, "is", self.battery, "%.")
        self.add_log("Battery reading: "+str(self.battery)+"%.")
    def speed_sensor(self):
        print("Current speed of drone", self.name, "is", self.speed, "km/h.")
        self.add_log("Speed reading: "+str(self.speed)+" km/h.")
    def temperature_sensor(self):
        temp=random.randint(30,70)
        print("Current temperature of drone", self.name, "is", temp, "°C.")
        self.add_log("Temperature reading: "+str(temp)+"°C.")
    def gyroscope_sensor(self):
        pitch=random.randint(-10,10)
        roll=random.randint(-10,10)
        yaw=random.randint(0,360)
        print("Gyroscope readings of drone", self.name, "- Pitch:", pitch, "°, Roll:", roll, "°, Yaw:", yaw, "°.")
        self.add_log("Gyroscope readings - Pitch: "+str(pitch)+"°, Roll: "+str(roll)+"°, Yaw: "+str(yaw)+"°.")                        
    def add_log(self,message):
        self.logs.append(message)
        print("Log added for drone", self.name)
    def show_logs(self):
        print("Logs for drone", self.name)
        for log in self.logs:
            print("-", log) 



d = Drone("phantom", 100, 0, 0)

while True:
    print("\n=== DRONE CONTROL MENU ===")
    print("1. take off")
    print("2. land")
    print("3. increase altitude")
    print("4. decrease altitude")
    print("5. increase speed")
    print("6. decrease speed")
    print("7. move north")
    print("8. move south")
    print("9. move east")
    print("10. move west") 
    print("11.show status")
    print("12.sensors")
    print("13.show logs")
    print("0. exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        d.take_off()        
    elif choice == "2":
        d.land()
    elif choice == "3":
        meters = int(input("Enter meters to increase altitude: "))
        d.increase_altitude(meters)
    elif choice == "4":
        meters = int(input("Enter meters to decrease altitude: "))
        d.decrease_altitude(meters)
    elif choice == "5":
        kmph = int(input("Enter km/h to increase speed: "))
        d.increase_speed(kmph)
    elif choice == "6":
        kmph = int(input("Enter km/h to decrease speed: "))
        d.decrease_speed(kmph)
    elif choice == "7":
        meters = int(input("Enter meters to move north: "))
        d.move_north(meters)
    elif choice == "8":
        meters = int(input("Enter meters to move south: "))
        d.move_south(meters)
    elif choice == "9":
        meters = int(input("Enter meters to move east: "))
        d.move_east(meters)
    elif choice == "10":
        meters = int(input("Enter meters to move west: "))
        d.move_west(meters)
    elif choice == "11":
        d.show_status()
    elif choice == "12":
        d.altitude_sensor()
        d.battery_sensor()
        d.speed_sensor()
        d.temperature_sensor()
        d.gyroscope_sensor()
    elif choice == "13":
        d.show_logs()
    elif choice == "0":
        print("Exiting drone control.")
        break
    else:
        print("Invalid choice. Please try again.")