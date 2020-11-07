

### door, light, x, y
### speed

### pipe, stair, water_weight
### sound, sprinkle
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
class Car():
    def __init__(self, door, light, color):
        self.door = door
        self.light = light
        self.color = color
        self.x = 0
        self.y = 0
        self.speed_x = 10
        self.speed_y = 20
        
        
    def run(self):    
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        
class FireTruck(Car):
    def __init__(self, door, light, color, water_weight):
        super().__init__(door, light, color)
        self.pipe = False
        self.stair = False
        self.water_weight = water_weight
        
    def sprinkle(self):
        print('sprinkle')
        self.water_weight = self.water_weight - 1
        
    def soundPlay(self):
        print('start playing sound')
        
        
        
car1 = Car(4, False, YELLOW)
fireTruck1 = FireTruck(2, False, RED, 1000)

print(car1.x)
print(car1.y)
for i in range(10):
    car1.run()  
print(car1.x)
print(car1.y)
print('start')
print(fireTruck1.water_weight)
for i in range(30):
  fireTruck1.sprinkle()
print('end')
print(fireTruck1.water_weight)

for i in range(20):
    fireTruck1.run()
print(fireTruck1.x)
print(fireTruck1.y)