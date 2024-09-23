#making list in python
#basically assigning multiple values/strings in one variable
#list always starts from 0



subjects = ["Maths", "Chemistry", "Physics", "English", "Linux", "Ethical Hacking"]

print(subjects)
print()
print(subjects[0])
print(subjects[4])

#printing a range of element from list

print(subjects[-2])



#also changing the items under tht variable
subjects[2] = "Digital logic"
print(subjects)

subjects.append("Python")
print(subjects)

subjects.remove("Python")
print(subjects)

subjects.insert(0,"Psychology")
print(subjects)


print(subjects.sort())

subjects.clear()#clears everything in the list
print(subjects)