def missingNumber(self, nums: List[int]) -> int:
        check_list=[i for i in range(len(nums)+1)]
        for i in nums:
            check_list.remove(i)
        return check_list[0]
