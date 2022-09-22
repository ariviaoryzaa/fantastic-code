# bilangan prima 1-100

for x in range (2,200):
    if x == 2:
        print(x)
    else:
        for y in range (2,x):
         if (x % y) == 0:
            break
        else: 
            print (x)
    
    
    path = r'./hello.txt'
for x in range(1, 100000, 2):
    file = open(path, "a")
    if x == 1:
        file.writelines("2")
    else:
        for y in range(2,x):
            if (x % y) == 0:
                break
        else:   
            file.writelines(str(x) + "\n")