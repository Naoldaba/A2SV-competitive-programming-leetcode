class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        di={}
        arr=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if di.get(i)==None:
                    if nums[j]<nums[i]:
                        di[i]=1
                else:
                    if nums[j]<nums[i]:
                        di[i]+=1
            if di.get(i)==None:
                arr.append(0)
            else:
                arr.append(di.get(i))
        return arr
