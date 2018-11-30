import random 
for x in range(30):
    a_list = [] 
    while len(a_list) < 25:
        r = random.randint(1,25) 
        if r not in a_list: 
            a_list.append(r) 
#    print(a_list)
    print(a_list[0:5])
    print(a_list[5:10])
    print(a_list[10:15])
    print(a_list[15:20])
    print(a_list[20:25])
    print('\r')