class Solution:
    def minInsertions(self, s: str) -> int:
        open_needed=0
        insertion=0
        i=0
        while i<len(s):
            if s[i]=="(":
                open_needed+=2
                i+=1
            else:
                if i<len(s)-1 and s[i+1]==")":
                    i+=2
                else:
                    insertion+=1
                    i+=1
                
                if open_needed>0:
                    open_needed-=2
                else:
                    insertion+=1
        return open_needed+insertion

        # ()) is a valid 
        #  if ( we need 2 more ")" and needed+2 and move pointer by 1 
        #       if ) and immediate next char is also ) 
        #       it is a valid so we move the pointer by 2
        #       if it ")" only one means  we needed ")" another to make it valid so insertion needed 
        #           is incremented by 1
        #       and if needed is greater than two means "(" this part is still waiting for its "))" pair so er decrement else incremented the insertion 
        