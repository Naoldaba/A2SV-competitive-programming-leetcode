def sortColors(self, nums: List[int]) -> None:
        prim,middle=0,0
        last=len(nums)-1
        while(middle<=last):
            if nums[middle]==0:
                nums[middle],nums[prim]=nums[prim],nums[middle]
                middle+=1
                prim+=1
            elif nums[middle]==1:
                middle+=1
            else:
                nums[middle],nums[last]=nums[last],nums[middle]
                last-=1
