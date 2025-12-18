def student_info(*args, **kwargs):
    return args,kwargs

print(student_info('Math', 'Arts', name = "kelvin", age = 23))

#V2
courses = ('Math', 'English', 'Science')
info = {'name': 'kelvin', 'age': 23, 'class': '2s10'}

def student_infos(*args, **kwargs):
    print(args)
    print(kwargs)

student_infos(*courses, **info)