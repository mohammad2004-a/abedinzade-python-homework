# person = ["mohammadm","ali","javad"]
# person.insert(2,"asghar")
# print(person)


# numbers =[1,5,6,4,89,9,65,564,45].sort()
# print(numbers)



person = {
    "first_name":"mohammad",
    "last_name":"abedinzadeh",
    "nationality":"iran",
    "birthday": 2004
}
print(person.setdefault("first_name","mahdi"))

for entry,value in person.items():      
    print(f"{entry:<10} : {value:>10}")


