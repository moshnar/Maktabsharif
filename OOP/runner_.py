import random
import time

class Runner:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
        self.x =0
        self.winner = False

    def step (self):
        if self.x <=10:
            self.x += self.speed * random.random()
        elif self.x >= 10:
            self.winner = True
            print(f'{self} is a winner!')

    def __str__(self):
        return '{} , {}'.format(self.name ,self.x)


r1 = Runner('ali',2)
r2 = Runner('abbas',3)
r3 = Runner('mohammad',4)

l = [r1,r2,r3]
flag = True
while flag:
     for i in l:
         i.step()
         print(f' {i.name} is in  {i.x}')
         time.sleep(1)
         if i.winner==True:
             flag = False
             break


