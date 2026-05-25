class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        mailbox=[[] for _ in range(len(nums)+2)]

        for number,frequency in counts.items():
            mailbox[frequency].append(number)

        result=[]
        for freq in range(len(mailbox)-1,0,-1):
            for number in mailbox[freq]:
                result.append(number)
            if len(result)==k:
                return result          