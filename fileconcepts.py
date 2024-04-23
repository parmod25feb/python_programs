# This progam is to understand the file functions


f = open("python_programs/datasource.txt","a")

tx = '''\n\nfile_name  The file_name argument is a string value that contains the name of the file that you want to access.

access_mode  The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. This is an optional parameter and the default file access mode is read (r).\n\n'''

f.write(tx)
print ("Closed or not: ", f.closed)

f.close()
print ("Closed or not: ", f.closed)
f = open("python_programs/datasource.txt","r")

txt =f .read()
print(txt)

