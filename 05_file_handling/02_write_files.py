# Python gives us the functionality to write to external files.


# This creates and opens a write_files.txt file
empty_file = open('05_file_handling/write_files.txt', 'w')

#This writes the texts in string in the external file
empty_file.write("This is the written text")
