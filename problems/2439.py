


#이전에 했던 것에 비해 첫쨰자리가 아닌마지막자리에서
#오는 것을 제외하고는 다 똑같다



N = int(input())
a = ""

for i in range(1,N+1): #몇 칸을 출력할 것인지
    for j in range(i): # 몇 번 반복할 것인지
        a +=('*'.rjust) #오른 쪽에서부터 찍을 방법
    a +="\n"
print(a)

