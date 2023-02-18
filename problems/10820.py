
while True:
    a = input()
    if a[-1] == ' ':
        break

    try:


        

    except:
        break


b = 0
c = 0
d = 0
e = 0
for i in range(len(a)):
    if a[i] == ' ':
        b += 1        #공백의 개수

    elif a[i].isdigit():
        c += 1

    elif a[i].islower():
        d += 1
    else:
        e += 1

print(d ,e ,c ,b ,end =' ')






