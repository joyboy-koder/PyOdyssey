# Python gives us the functionality to read from external files like csv,txt.etc


# You first open the file by passing in the name of the file with extension and also a mode (r)

workers_record = open("05_file_handling/read_files.txt", "r")

# Dispaly what's in read_files.txt with the print() and read() functions
print(workers_record.read())
