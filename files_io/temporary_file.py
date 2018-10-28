#Temporary file

'''
w+ = reading and writing the same time
with auto destroyed  when file closed
'''

from tempfile import TemporaryFile

with TemporaryFile('w+') as fobj:
    fobj.write("Life is cool. \n")
    fobj.seek(0) #seek to the beginning
    data=fobj.read()
    print(data)