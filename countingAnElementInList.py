backpack = ['sword', 'rubber duck', 'slice of pizza', 'parachute', 'slice of pizza']

print(backpack)

# print(backpack.count('slice of pizza'))

if backpack.count('slice of pizza') <5:
  backpack.append('slice of pizza')

print(backpack)

if 'sword' not in backpack:
  print('yes')