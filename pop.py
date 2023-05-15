workdays = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

workdays.insert(2, "wednesday")

print(workdays)

popped = workdays.pop(1)
print("we just popped '" + popped + "' out.")

print(workdays)