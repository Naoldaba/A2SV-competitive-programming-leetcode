def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out=[]
        for j in range(len(nums)):
            cout=0
            for i in range(len(nums)):
                if nums[j]>nums[i]:
                    cout+=1
            out.append(cout)
        return out
