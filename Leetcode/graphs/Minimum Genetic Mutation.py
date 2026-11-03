class Solution:
    def minMutation(self, start: str, end: str, wordList: list[str]) -> int:
        
        if start==end or not wordList:
            return -1
        
        wordList.append(start)
        allWords=wordList
        words=set(wordList)
        
        adj=defaultdict(list)
        for word in allWords:
            for i in range(len(word)):
                for char in "ACGT":
                    if i==char:
                        continue
                    nextWord=word[:i]+char+word[i+1:]
                    if nextWord in words:
                        adj[word].append(nextWord)
        
        queue=deque()
        visited=set()
        queue.append(start)
        visited.add(start)
        value=0
        while queue:
            value+=1
            for _ in range(len(queue)):
                node=queue.popleft()
                for neigh in adj[node]:
                    if neigh==end:
                        return value
                    
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
        return -1        