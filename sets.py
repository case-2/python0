backpack = ['sword', 'rubber duck', 'slice of pizza', 'parachute', 'slice of pizza']
# backpack2 = {'sword', 'rubber duck', 'slice of pizza', 'parachute', 'slice of pizza'}

backpack2 = {''}

for i in backpack:
  backpack2.add(i)

print(backpack2)

print('slice of pizza' in backpack2)
print('' in backpack2)