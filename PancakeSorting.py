def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for i in range(n):
            cur_max = max(arr[:n-i])
            j = arr.index(cur_max)

            arr[:j+1] = reversed(arr[:j+1])
            res.append(j+1)

            arr[:n-i] = reversed(arr[:n-i])
            res.append(n-i)
        return res
