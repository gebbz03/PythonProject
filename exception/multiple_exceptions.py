#Multiple Exceptions

try:
    disk_file=open('filename')
except(FileNotFoundError,PermissionError): #using tuple
    print("Cannot open the file")


try:
    disk_file=open('filename')
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("Permision denied")              