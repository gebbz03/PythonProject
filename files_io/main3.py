
#reading line by line and make uppercase
with open("article.txt") as fobj:
    for num, line in enumerate(fobj):
        print(num+1,line.upper())