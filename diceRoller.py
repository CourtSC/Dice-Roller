from random import randint
import sys

# TODO: Check for advantage and disadvantage.

# Ask user for input.
while True: # Main program loop
    try:
        diceStr = input('> ') # Prompt for input as string.
        if diceStr.upper == 'QUIT':
            sys.exit

        # Clean up input.
        diceStr = diceStr.lower().replace(' ','')

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

        # Simulate dice rolls.
        rolls = []
        for roll in range(numberOfDice):
            rolls.append(randint(1,sizeOfDice))

        # Display the total.
        print(f'Total: {sum(rolls) + diceMod}')
        if len(rolls) > 1:
            print(f'Rolls: {rolls}')
        if diceMod != 0:
            print(f'Modifier: {modSign}{abs(diceMod)}')

        # Verbose testing.
        # print(f'modSignIndex Value: {modSignIndex}')
        # print(f'modSign Value: {modSign}')
        # print(f'diceMod Value: {diceMod}')

    except Exception as exc:
        # Catch any exceptions and display to user.
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue  # Go back to the dice string prompt.