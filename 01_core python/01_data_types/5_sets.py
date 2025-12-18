#Unordered and no duplicate

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

#Intersection
#Union
#Difference

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'OWOP'}

print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))
print(cs_courses.difference(art_courses))

#Empty set
empty_set = {} #This isnt right, its a dict..
empty_set = set()