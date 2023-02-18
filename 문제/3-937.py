from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        list_str = []
        list_int = []
        for i in range(len(logs)):
            if logs[i].split()[1].isalpha():
                list_str.append(logs[i])
            else:
                list_int.append(logs[i])

        list_str.sort(key=lambda log: (log.split()[1:], log.split()[0]))
        # 정렬 기준이 하나면, 괄호로 안 묶어도 되는데,
        # 정렬 기준이 여러개면 괄호로 묶어야 된다.

#풀이1
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters , digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits


s = ['2A', '1B', '4C','1A']



#def func(x):
#    return x.split()[1], x.split()[0]

#질문) 람다에 의한 결과물 출력하는법
s.sort(key=lambda x: (x.split()[1], x.split()[0]))
#print(s.sort(key=lambda x: (x.split()[1], x.split()[0])))

