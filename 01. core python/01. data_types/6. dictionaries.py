#Dictionaries

student = {'name': 'Kelvin', 'class': 'Grade_12', 'age': 19}
print(student)
print(student['name'])
print(student['class'])

#Acessing key
print(student.get('age'))

#Add new entry
student['height'] = 7
student['complexion'] = 'fair'
print(student)

#Updating
student.update({'class': 'Grade_13', 'age': 20})
print(student)

#Deleting
del student['age']
print(student)
height = student.pop('height')
print(height)
print(student)

#loop through
for key, value in student.items():
    print(key, value)