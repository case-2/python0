# print(len(["hi", "hello", "wassup"]))

greetings = ["hi", "hello", "wassup"]

print(len(greetings))

#n --> list size
#highest index = n-1
print(greetings[2])

for i in range(len(greetings)):
  print(i, greetings[i])

for i in greetings:
  print(i)