 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        li=[]
        for lap in intervals:
            if li and lap[0]<=li[-1][1]:
                li[-1][1]=max(li[-1][1],lap[1])
            else:
                li.append(lap)
        return li
