#return value

def square (num):
    return num * num
print(square(2),square(2.2),sep='|')    
print("-------------------------")

#return getter

def get_name(fname,lname):
    return fname+" "+lname

print(get_name("Gebb","Ebero"))
print(get_name("Edelyn","Garcia"))    
print("-------------------------")

#Optional argument

def gname(fname,lname,mname=''):
    cname=fname
    if mname:
        cname +=' '+mname

    cname += ' '+lname
    return cname

print(gname("Gebb","Ebero"))
print(gname("Gebb","Ebero","H"))