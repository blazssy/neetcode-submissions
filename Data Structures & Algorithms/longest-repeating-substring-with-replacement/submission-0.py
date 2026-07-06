class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpp={}
        l=0
        res=0
        for r in range(len(s)):
            mpp[s[r]]=mpp.get(s[r],0)+1
            window_length=r-l+1
            max_freq=max(mpp.values())
            while window_length-max_freq>k:
                mpp[s[l]]-=1
                l+=1
                window_length=r-l+1
            res=max(res,r-l+1) 
        return res       
