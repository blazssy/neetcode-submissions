from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        res=[]
        left=right=0
        for right in range(len(nums)):
            #calculate the left of the window
            left=right-k+1
            # remove left if it is experied 
            while dq and dq[0]<left:
                dq.popleft()
            # now check for the smaller elemnt and pop it     
            while dq and nums[dq[-1]]< nums[right]:
                dq.pop()
            # after poping add the new element(we are storing the index not the element)   
            dq.append(right)    
            #now add the element in the 
            if right>=k-1:
                res.append(nums[dq[0]])
        return res

        