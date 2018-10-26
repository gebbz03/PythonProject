#Matching text at start and at end

filename="bigdata.txt"
print(filename.endswith('.txt'))
print(filename.startswith('bi'))

print("---------------------------------------------------------")


#Find word in a sentence

sentence="A quick brown fox jumps over the lazy dog"

print(sentence.find("fox"))
print(sentence.find("foxs")) #return -1, not found

sentence=sentence.replace("fox","tiger")
print(sentence)

print("---------------------------------------------------------")


#Print Separator

x="Gebb Ebero"
y="Edelyn Garcia"
z="Boyie Maming"

print(x+" | "+y+" | "+z)
print(x,y,z,sep=" | ")

