'''
Docstring for 03_error_handling.try_except
The "try", "except" in python helps to output the specific type of error made by the user or programmer instead of the traditional python error statement in the terminal.
'''


try:
    #An error output since a number can't be divided by 0
    answer = 10/0

    #An error output if the user types in another datatype instead of an int
    #Comment out the previous code to experience this.
    number = int(input('Input a number: '))
    print(number)

except ValueError:
  #A specific error message when the user types in a string instead
  print('invalid Input')

except ZeroDivisionError:
   #A specific error message when 10/0 runs
   print('Divided by zero')