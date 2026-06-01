# A class that represents a ROBOT
# with properties and actions

# Think of it like:
# ├─ Properties (what it HAS):
# │  ├─ Name (R2D2, C3PO, etc.)
# │  ├─ Model (type of robot)
# │  ├─ Battery level (100%, 50%, etc.)
# │  └─ Position (where it is: x, y)
# │
# └─ Actions (what it CAN DO):
#    ├─ Move to new position
#    ├─ Check if it has enough battery
#    ├─ Charge itself
#    └─ Report its status
import math
import time

class Robot:
    
    def __init__(self,name,model):
        self.battery_level = 100
        self.position = [0,0]
        self.name= name 
        self.model = model
    def Charge(self):
        print("CHARGING GOING ON PLEASE WAIT....")
        count=0
        self.battery_level=100
        while True:
            print(".............charging.............")
            time.sleep(2)
            count+=1
            if count ==5:
                print("CHARGING COMPLETED...")
                break
        
    def Move(self,x,y):
        self.x= x
        self.y = y
        print(f"{self.name} - {self.model} IS AT ({self.x},{self.y}) POSITION ")
        distance = math.sqrt(x**2 + y**2)
        if distance >250:
            distance=distance-250
        # using convension for every 5 distance battery will be reduced by 2%
        battery_used=float((distance/5)*2)
        if self.battery_level >=battery_used :
            self.position=[x,y]
            self.battery_level-= battery_used
            print(f"REMAINING BATTERY:- {self.battery_level:.2f} %")
        elif self.battery_level< battery_used and battery_used<100:
            print("NEED TO CHARGE BATTERY TO REACH THE POSITION")
            Robot.Charge(self)
        elif self.battery_level <20:
            print("WILL GET DISCHARGED SOON! NEED TO BE CHARGED")
            print(f"REMAINING BATTERY:- {self.battery_level:.2f} %")
        elif self.battery_level<10:
            print(f"{self.name}-{self.model} has discharged in between and can't reach the position")
            Robot.Charge(self)
            battery_used==0
        self.position == (self.x,self.y)
    def status(self):
        print("--------ROBOT CURRENT STATUS--------")
        print(f"{self.name} ({self.model}), current position {self.position} , battery level {self.battery_level}")
if __name__=="__main__":

    robot=Robot("WATER_SURFACE_CLEANING","controlled")
    robot.status()
    print()
    robot.Move(10,15)
    print()
    robot.Move(100,70)
    print()
    robot.Move(100,100)
    print()
    robot.Move(200,200)
    print()
    robot.status()

    


        
