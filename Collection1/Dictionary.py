# dic={
#     "name":"vikram",
#     "age": 19,
#     "subject":['java','python'],      #with touple use
#     20 : 88.4

# }
# print(dic)
# print(type(dic))
# dic["name"]="Shobh"
# print(dic)

student={
    "name":"Vikram",
    "marks":{
        "phy":79,
        "his":90,
        "math":60
    }
}
# print(student)
# print(student["marks"])
# print(student["marks"]["math"])

print(student.keys())
print(len(student))

print(student.values())


print(student.items())

# print(student["name2"])    #error
# print(student.get("name2"))   # no error    = none print

student.update({"city":"pune"})
print(student)






