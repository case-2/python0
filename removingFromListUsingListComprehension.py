healthy = ['kale chips', 'broccoli'] # lookup list
backpack = ['pizza', 'frozen custard', 'apple crisp', 'kale chips']

backpack = [item for item in backpack if item in healthy] # reassigning backpack the variable, creates a new backpack variable in the memory with different id

backpack[:] = [item for item in backpack if item in healthy] # changing backpack the variable - [:] prevents python from creating a new list in the memory

print(backpack)
