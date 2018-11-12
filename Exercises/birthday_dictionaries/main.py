from birthdays import *

print("================================")
print("Welcome to the Birth-Date Database")
print("================================")

print("\nWe have records for:")
for item in birthdays:
    print(item)
    
name = str(input("Enter a name to obtain a birth-date >> "))
if birthdays[name] != "":
    print("\n" + name + "'s birth-date is " + birthdays[name])
else:
    print("No records exist for " + name)