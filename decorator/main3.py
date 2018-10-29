

def uppercase(function):
    def decorated(*args):
        result = function(*args)
        result_upper = result.upper()
        return result_upper
    return decorated    


@uppercase
def person_name(name):
    return name

upname=person_name("Gebb Ebero")
print(upname)