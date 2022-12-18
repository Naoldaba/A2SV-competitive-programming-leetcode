def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ind=[]
        for j in range(len(nums)):
            if nums[j]==target:
                ind.append(j)
        return ind
