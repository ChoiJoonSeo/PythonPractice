import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = [word for word in re.sub("[^0-9a-z]", ' ', paragraph).split() if word not in banned]

        a = Counter(paragraph)
        return a.most_common(1)[0][0]  #most common으로 되는것은 리스트 값으로
                                    #a.most_common(1) [('ball',2)]

        words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split()
                 if word not in banned]
        #질문) 이 문장에서 정규식 할때 왜 r이 처음 들어가는지
        #질문) if word not in banned 가 어떤 형식으로 맞는 문장이 된건지
             #질문)counts = collections.defaultdict(int)
             #질문)counts = 0 이라는 것이 쓰일 수 있는 것인지?
                for word in words:s
                    counts[word] += 1  #질문)이 형식이 키값에 대한 값을 더하는 것인가?