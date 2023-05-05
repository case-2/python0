healthy = ['kale chips', 'broccoli']
backpack = ['pizza', 'frozen custard', 'apple crisp', 'kale chips']

# backpack.remove('pizza') # stupid way

# smarter way
if "pizza" not in healthy:
  backpack.remove('pizza')

if "kale chips" not in healthy:
  backpack.remove('kale chips')

print(backpack)
