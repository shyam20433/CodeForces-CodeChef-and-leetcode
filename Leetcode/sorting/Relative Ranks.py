import heapq
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        res=[]
        heapq.heapify(res)
        for i,num in enumerate(score):
            heapq.heappush(res,(num,i))
        hash={ num:i for i,num in enumerate(score)}
        hash=dict(sorted(hash.items(),key=lambda x:x[0],reverse=True))
        print(hash)
        result=[""]*(len(score))
        count=1
        for num,index in hash.items():
            if count==1:
                result[index]="Gold Medal"
            elif count==2:
                result[index]="Silver Medal"
            elif count==3:
                result[index]="Bronze Medal"
            else:
                result[index]=str(count)

            count+=1
        return result

        