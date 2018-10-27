#Value type

num=100
def change_num(n):
    n += 100
    print(f"Inner num: {n}")

change_num(num)
print('Outside num: '+str(num))