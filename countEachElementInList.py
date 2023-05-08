backpack = ['sword', 'rubber duck', 'slice of pizza', 'parachute', 'slice of pizza', 'slice of pizza']

#counts = [backpack.count(item) for item in backpack]


counts = [[backpack.count(item), item] for item in set(backpack)]

print(counts)

# shorter way
[print(backpack.count(item), item) for item in set(backpack)]