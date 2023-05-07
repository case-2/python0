healthy = ['kale chips', 'broccoli']
backpack = ['pizza', 'frozen custard', 'apple crisp', 'kale chips']

backpack[:] = [item for item in backpack if item in healthy]

# if you do it the long way
# healthy_backpack = []

# for item in backpack:
#   if item in healthy:
#     healthy_backpack.append(item)


print(backpack)