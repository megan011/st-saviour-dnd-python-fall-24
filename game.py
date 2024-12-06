import time
from tav import Tav

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def generate_monster() -> int:
    ogre = '\U0001F479'
    print(ogre + ' A Demogorgan Apears! ' + ogre)
    print('Roll Required 10')
    return 10

if __name__ == '__main__':
    # collecting user input
    name = input('Name: ')
    role = input('Role: ')
    player = Tav(name,role)
    print('Bludgeons & Flagons')
    player.print_character_sheet()
    print_dramatic_text('Our story begins in the Upsidedown ...')
    requirement = generate_monster()
    print ('            ')
    print_dramatic_text('You wake up disoriented, pushing yourself up from the firm, cold ground. Everything around you is twisted, dark, and wrong. You brush the dirt off your pants and look into the empty horizon, with the air cold and thick with fog. A horrific screech mixed with a roar echoes from the mist ahead. You stand firm, and turn towards what seems to be a demogorgon.')
    print ('            ')
    weapons = ['Telekinesis', 'Bat', 'Slingshot']
    print(weapons)
    weapon = input('What weapon will you use?')
    
    # TODO - accept buffs from user
    buff = input('Enter \'a\' for advantage, \'g\' for guidance or Enter to roll: ')
    if player == 'a': 
        print ('advantage roll')

    elif player == 'g': 
        print ('guidance roll')

    else: 
         print ('enter roll')

    roll = player.roll()


    if player == 'a': 
        print ('advantage roll')

    elif player == 'g': 
        print ('guidance roll')

    else: 
         print ('enter roll')

    roll = player.roll()

    if requirement <= roll:
        print ('You win!')

    if requirement > roll: 
        print ('You lost!')

    def generate_monster (Mindflayer: str, roll_required: int) -> int:
        print(f"{'👻'} {Mindflayer} Appears! {'👻'}")
        print(f"Roll Required {roll_required}")
        return roll_required

    print ('            ')
    print (' 👻 A Mindflayer Apears! 👻')
    print ('Roll Required 10')

    print_dramatic_text('You feel a strong gust of wind and sense the presence of something terrible...')
weapons = ['Telekinesis', 'Bat', 'Slingshot']
print(weapons)
weapon = input('What weapon will you use for the Mind Flayer?')

print ('            ')

buff = input('Enter \'a\' for advantage, \'g\' for guidance or Enter to roll: ')
if buff == 'a':
  print ('Advantage roll for Mind Flayer')
elif buff == 'g':
  print ('Guidance roll for Mind Flayer')
else:
  print ('Normal roll')

roll = player.roll()

if buff == 'a':
  print ('Advantage roll')
elif buff == 'g':
  print ('Guidance roll')
else:
  print ('Normal roll')

if requirement <= roll:
  print ('you win!')
else:
  print ('You lost!')


if buff == 'a':
  print ('Advantage roll for Mind Flayer')
elif buff == 'g':
  print ('Guidance roll for Mind Flayer')
else:
  print ('Normal roll')

roll = player.roll()

if buff == 'a':
  print ('Advantage roll')
elif buff == 'g':
  print ('Guidance roll')
else:
  print ('Normal roll')

if requirement <= roll:
  print ('you win!')
else:
  print ('You lost!')