#아이디어
#오른쪽과 왼쪽에서 같은 높이까지 왔을떄 그 안에 있는 값들을 더하는 방식


left, right = 0
for i in range(len(height)):
    if height[left] =< height[right]:
        for i in range(left:right-1)
            += height[i]-height[i+1]
