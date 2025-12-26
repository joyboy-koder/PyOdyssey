# Python gives us the functionality to append texts to the end of external text file such as .txt,.csv etc


# The codes below opens the file and with the help of the mode 'a' for append and the function write(), new piece of texts are added to the end of a text file.

church_attendance = open("05_file_handling/append.csv", 'a')
church_attendance.write('\nThursday - 45  #This was what was recently appended')
church_attendance.write('\nThursday - 45  #This was what was recently appended')

# This closes the file when done!
church_attendance.close()

# The code below now reads and prints out the external file information after the above appending is completed
church_summary = open("05_file_handling/append.csv", "r")
print(church_summary.read())

# This closes the file when done!
church_summary.close()

