class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        start=0
        end=len(letters)-1
        if(letters[0]>target):
            new=0
        elif letters[-1]<=target:
            new=0
        else:

            while(start<=end):
                mid=start+(end-start)//2
                if letters[mid]<=target:
                    start=mid+1
                  
                else:
                    end=mid-1
                    
           
        return letters[start]