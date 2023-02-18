s = input()

# ord <= 아스키 코드를 돌려주는 함수
# ord('a') ~ ord('z')
loc = [-1 for i in range(ord('z') - ord('a') + 1)]

alpha = 'abcdefghikjlmnopqrstuvwxyz'
d = {s:-1 for s in alpha}

for i in range(len(s)):
    idx = ord(s[i]) - ord('a') # 아스키코드의 시작점을 빼주면서, 인덱스를 찾음
    if loc[idx] == -1: # 아직 초기값이 바뀌지 않았을 때만
        loc[idx] = i # 인덱스를 기록하겠다.

for i in range(len(s)):
    if d[s[i]] == -1:
        d[s[i]] = i
d.items() # 키-값을 쌍으로
d.keys() # 키만 쭉 리스트로 담아서 줌
d.values() # 값만 쭉 리스트로 담아서 줌

print(*d.values())
