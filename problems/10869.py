a, b = map(int,input().split())
answer = [a+b, a-b, a*b, a//b, a%b]
# for num in answer:
#     print(num)
print('\n'.join(answer))
#10869
#\n 을 어떻게 넣어야지 아래로 가나?
# -> print를 여러번 하는 것보다, 답을 하나의 리스트에 담고
# join을 사용해서 하나의 문자열로 합친 후 print 한번하기