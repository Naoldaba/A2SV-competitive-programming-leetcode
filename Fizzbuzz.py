class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li=[]
        st=""
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                st="FizzBuzz"
                li.append(st)
                continue
            elif i%3==0:
                st="Fizz"
                li.append(st)
                continue
            elif i%5==0:
                st="Buzz"
                li.append(st)
                continue
            li.append(str(i))
        return li
