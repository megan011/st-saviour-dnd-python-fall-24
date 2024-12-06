import random
from draw import draw_d20, draw_d4

class Tav: 
    def __init__ (self, name: str, role: str ):
        self.name = name 
        self.role = role 

        self.level = 1

        self.strength = 0 
        self.wisdom = 0 
        self.charisma = 0 
        self.intelegence = 0 
        self.consitution = 0 
        self. dexterity = 0 

        self.assign_stats()

    def print_character_sheet(self): 
        print('Name: ' + self.name)
        print('Role: ' + self.role)
        print('Level: ' + str(self.level))
        print('------------------------')
        print('Strength: ' + str(self.strength))
        print('Dexterity: ' + str(self.dexterity))
        print('Intelegence: ' + str(self.intelegence))
        print('Consitution: ' + str(self.consitution))
        print('Wisdom: ' + str(self.wisdom))
        print('Charisma: ' + str(self.charisma))

    def assign_stats(self):
        stats = [15, 14, 13, 12, 10, 8]
        random.shuffle(stats)
        self.strength = stats[0]
        self.dexterity = stats[1]
        self.intelegence = stats[2]
        self.charisma = stats[3]
        self.widsom = stats[4]
        self.constitution = stats[5]

    def roll(self) -> int:
       r = random.randint(1, 20)
       draw_d20(r)
       return r
  
    def roll_advantage(self) -> int:
       r = random.randint(1, 20)
       draw_d20(r)


       s = random.ranint(1, 20)
       draw_d20(s)


       if r > s:
           return r
       return s
  
    def roll_guidance() -> str:
       r = random.randint(1, 20)
       draw_d20(r)
       s = random.randint(1, 4)
       draw_d4(s)
      
       return r + s






