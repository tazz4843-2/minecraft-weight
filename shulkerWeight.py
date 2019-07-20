import math
layers = int(raw_input('Select how many shulker boxes you would like: '))

if (layers > 216):
    print('****ERROR: Weight has overflowed and is now beyond infinity****')
    print('Exiting with error code 1')
    exit(1)

if (layers > 212 and layers < 216):
    print('**WARN: Weight is equal to inf (infinity)**')

weight = 0 # Total weight
blockName = 'gold' # Set to the block name
first = 37*27*64 # Filling the inventory full of shulker boxes full of said block
blockWeight = 19300 # Weight of said block in kilograms

layers = layers - 1
if (layers == 0):
    total = first * blockWeight
    print(total)
else:
    power = math.pow(27,layers)
    total = first * power
    print('Total weight of ' + blockName + ' in ' + str(layers+1) + ' shulker boxes is equal to ' + str(total) + ' kg or ' + str(total/1000) + ' tons.')

r = 0 # Radius of the event horizon (if greater than 1.80m, Steve is a black hole)
c = 299792458 # Speed of light (used to calculate radius of event horizon)
G = 6.67408E-11 # Gravitational constant
M = total + 60 # Weight of all the blocks plus Steve's weight [150lbs or 60kg])

# Formula for radius of event horizon is r = 2GM/c^2
r = 2 * G * M / math.pow(c,2)

if (r > 1.8): # If radius of event horizon is greater than 1.8m, Steve is a black hole.
    print('Steve is a black hole! :)')
else:
    print('Steve is not a black hole. :(')
