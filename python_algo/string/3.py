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


Solution().reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])