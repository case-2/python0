workdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

print(workdays, id(workdays))

workdays[:] = ["jlsdjflja"]

print(workdays, id(workdays))

workdays = ["kdsjjf", "kdlsjfalj"]

print(workdays, id(workdays))

workdays2 = workdays[:]

print(workdays2, id(workdays2))