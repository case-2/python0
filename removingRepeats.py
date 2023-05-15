import time

go = time.time()
workdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

print(set(workdays))

for item in set(workdays):
  while workdays.count(item)>1:
    workdays.remove(item)

print(workdays)

# print(len(set(workdays)))

# newList=[]
# for el in workdays:
#   if el not in newList:
#     newList.append(el)
#   elif len(newList) == len(set(workdays)):
#     print(newList)
#     break

print(time.time()-go)
