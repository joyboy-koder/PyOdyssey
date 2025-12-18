#Comaprisons
#Equal : ==
#Not Equal : !=
#Greater Than : >
#Less Than : <
#Greater or Equal : >=
#Less or Equal : <=
#Object identity : is

if True:
    print('Conditional was True')

language = 'Python'
if language == 'Python':
    print('Language is Python')

weather = 'rainy'
if weather == 'rainy':
    print('Weather is rainy')
else:
    print('Weather is not rainy')

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')

# and, or, not

user = 'kev'
logged_in = True

if user == 'Admin' and logged_in:
    print('Logged in as Admin')
else:
    print('Bad credentials')

logged_in = False

if not logged_in:
    print('Please log in')
else:
    print('Logged in')

### is
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

#Because...
print(id(a))
print(id(b))
# Different addresses in memory