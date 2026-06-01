# A class that represents a SENSOR
# that collects data over time

# Think of it like:
# ├─ What it HAS (properties):
# │  ├─ Sensor type (temperature, distance, motion, etc.)
# │  └─ List of readings (all data collected)
# │
# └─ What it CAN DO (actions):
#    ├─ Add a reading to the list
#    ├─ Calculate average of all readings
#    ├─ Find highest reading
#    ├─ Find lowest reading
#    └─ Clear all readings
class Sensor:
    def __init__(self,type):
        self.type=type
        self.readings=[]
    def get_readings(self,reading):
        self.reading=reading
        try :
            self.readings.append(float(self.reading))
        except:
            print("invalid reading")
        return self.readings
    def average(self):
        self.sum=0
        for i in self.readings:
            self.sum+=i
        average = self.sum/len(self.readings)
        return average
    def highest(self):
        highest_reading = max(self.readings)
        return highest_reading
    def lowest(self):
        lowest_reading = min(self.readings)
        return lowest_reading
    def clear(self):
        self.readings.clear()
        return "READINGS CLEARED"
sensor1 = Sensor("temperature")
sensor1.get_readings("PIZZA")
sensor1.get_readings(40)
sensor1.get_readings(30)
sensor1.get_readings(20)
print(sensor1.average())
print(sensor1.highest())
print(sensor1.lowest())
print(sensor1.clear())

