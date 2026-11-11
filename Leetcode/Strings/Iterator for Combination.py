class CombinationIterator:

    def __init__(self, characters: str, k: int):
        
        self.res=[]
        def backtrack(sol,k,start):
            if len(sol)==k:
                self.res.append("".join(sol))
                return
            
            for i in range(start,len(characters)):
                sol.append(characters[i])
                backtrack(sol,k,i+1)
                sol.pop()
        backtrack([],k,0)
        print(self.res)

        

    def next(self) -> str:
        return self.res.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.res)>0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()