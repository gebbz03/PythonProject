try:
    fobj=open('article.txt')
except Exception as e:
    print("File error: ",e)
else:
    contents=fobj.read()
    print(contents)
finally:
    fobj.close()            