from random import randint
import sys

# This is a change.

# Dice rolling function.
def diceRolls():
    rolls = []
    for roll in range(numberOfDice):
        rolls.append(randint(1,sizeOfDice))
    return rolls

# Ask user for input.
while True: # Main program loop
    try:
        diceStr = input('Enter something like "3d6" or "1d10+2".\n>') # Prompt for input as string.
        if diceStr.upper() == 'QUIT':
            sys.exit()
            
        # TODO: Add a help dialogue.
        # TODO: Allow rolling multiple different dice at once. Ex: 1d4 + 1d6

        # Clean up input.
        diceStr = diceStr.lower().replace(' ','')
        # Check for Advantage (roll twice and take the higher value).
        advIndex = diceStr.find('adv')
        diceStr = diceStr.replace('adv','')
        # Check for Disadvantage (roll twice and take the lower value).
        disIndex = diceStr.find('dis')
        diceStr = diceStr.replace('dis','')

        # Find the index of "d" in the input.
        dIndex = diceStr.find('d') # The index of the "d" character.
        if dIndex == -1:
            raise Exception ('Missing the "d" character.')
        
        # Find the number of dice.
        numberOfDice = int(diceStr[:dIndex])

        # Find the index of the modifier if one exists. Find the modifier.
        if '+' in diceStr: # There is a '+' modifier.
            modSignIndex = diceStr.find('+')
            modSign = '+'
            diceMod = int(diceStr[modSignIndex + 1:])
        elif '-' in diceStr: # There is a '-' modifier.
            modSignIndex = diceStr.find('-') 
            modSign = '-'
            diceMod = -int(diceStr[modSignIndex + 1:])
        else: # There is no modifier.
            modSignIndex = -1 
            modSign = '+'
            diceMod = 0

        # Find the size of the dice.
        if modSignIndex == -1: # There is no modifier to the roll.
            sizeOfDice = int(diceStr[dIndex + 1:])
        else:
            sizeOfDice = int(diceStr[dIndex + 1: modSignIndex])

        # Display the total.
        if advIndex != -1 or disIndex != -1:
            roll1 = diceRolls()
            roll2 = diceRolls()

        if advIndex != -1: # Roll with Advantage.
            rolls = max(roll1,roll2)
            print(f'Total: {sum(rolls) + diceMod}')
            advRolls = '\u0336'+'\u0336'.join(str(min(roll1, roll2)))
            print(f'{rolls}, {advRolls}')

        elif disIndex != -1: # Roll with Disadvantage.
            rolls = min(roll1, roll2)
            print(f'Total: {sum(rolls) + diceMod}')
            disRolls = '\u0336'+'\u0336'.join(str(max(roll1, roll2)))
            print(f'{rolls}, {disRolls}')

        else: # Roll normally.
            rolls = diceRolls()
            print(f'Total: {sum(rolls) + diceMod}')
            print(f'Rolls: {rolls}')
            
        if diceMod != 0:
            print(f'Modifier: {modSign} {abs(diceMod)}')
        print('\n')

        # Verbose testing.
        # print(f'modSignIndex Value: {modSignIndex}')
        # print(f'modSign Value: {modSign}')
        # print(f'diceMod Value: {diceMod}')

    except Exception as exc:
        # Catch any exceptions and display to user.
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue  # Go back to the dice string prompt.