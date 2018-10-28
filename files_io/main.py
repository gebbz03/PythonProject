try:
    with open('article.txt') as fobj:
        contents = fobj.read()
        print(contents)

except Exception as e:
    print("File Error: ",e)        