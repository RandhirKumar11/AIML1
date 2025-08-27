# creation of  a dictionary
student={"name":"Shreya","age":24, "course":"python"}

#Accessing
print(student["name"])
print(student)
print(student.get("age"))
print(student.get("marks","Not found"))

# adding and updating
student["marks"]=95
student["age"]=22
print(student)

# Removing
student.pop("course") #it will remove key course
print(student)

student.popitem() #remove last insert
print(student)

del student["age"] # remove key age
print(student)

student.clear() # remove all items
print(student)

# Dictionary view
print("\n\n\nDictionary view Operation")
student={"name":"Rana","age":21,"course":"AIML"}
print(student.keys())
print(student.values())
print(student.items())

# coping
new_dict=student.copy()
print(new_dict)

# Set default
student.update({"age":22,"city":"Delhi"})
print(student)

student.update({"name":"Randhir","age":22,"city":"Delhi"})
print(student)

# from keys
keys=["a","b","c"]
default_value=0
new_dict=dict.fromkeys(keys, default_value)
print(new_dict)