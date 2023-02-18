#for i in range(5, -1,-1):
#    print(i)
#5에서부터 0까지
import collections

#logs = logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#for log in logs:
#print(log)
#list가 풀려서 각각 저장됨

#s = ['2A', '1B', '4C','1A']



#def func(x):
#    return x.split()[1], x.split()[0]


#s.sort(key=lambda x: (x.split()[1], x.split()[0]))
#print(s.sort(key=lambda x: (x.split()[1], x.split()[0])))


strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = collections.defaultdict(list)

for word in strs:
    anagrams = ''.join(sorted(word)).append(word)

    print(list(anagrams.values()))
