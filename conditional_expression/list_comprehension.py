

num_squares=[v * v for v in range(1,11)]
print(num_squares)

print()

num_squares=[]
for v in range(1,11):
    num_squares += [v * v]
print(num_squares)    
print("------------------------------------------------------")


#odd numbers only
num_squares = [v * v for v in range(1,11) if v%2 != 0]
print(num_squares)
print("------------------------------------------------------")

#Dictionary expression
num_dict_sq={v: v * v for v in range(1,11) if v%2 != 0}
print(num_dict_sq)
print("------------------------------------------------------")

#Set expression
num_set_sq = {v *v for v in range(1,11) if v%2 != 0}
print(num_set_sq)

