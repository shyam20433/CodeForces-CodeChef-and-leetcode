from collections import defaultdict,deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        adj=defaultdict(list)
        wordList.add(beginWord)
        words=list(wordList)
        
        # def isConnected(word1,word2):
        #     count=0
        #     for i in range(len(word1)):
        #         if word1[i]!=word2[i]:
        #             if count>0:return False
        #             count+=1
        #     return True
        # O(n.n.l)=> too slow
        # for i in range(len(words)):
        #     for j in range(i+1,len(words)):
        #         word1=words[i]
        #         word2=words[j]
                
        #         if isConnected(word1,word2):
        #             adj[word2].append(word1)
        #             adj[word1].append(word2)

        # O(n.l.26)=>faster
        for word in words:
            for i in range(len(word)):
                curr=word[i]
                for char in "qwertyuiopasdfghjklzxcvbnm":
                    if curr==char:
                        continue
                    next_word=word[:i]+char+word[i+1:]
                    if next_word in wordList:
                        adj[word].append(next_word)
        
        #shortest path for bfs
        queue=deque()
        visited=set()
        visited.add(beginWord)
        queue.append(beginWord)
        level=0
        while queue:
            level+=1
            for _ in range(len(queue)):
                node=queue.popleft()
                
                for neigh in adj[node]:
                    if neigh==endWord:
                        return level+1
                    if neigh not in visited:
                        visited.add(node)
                        queue.append(neigh)
        return 0