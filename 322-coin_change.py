class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        mem={0:0}

        def recal(amt):
            if amt in mem:
                return mem[amt]
            minn=float('inf')
            for i in coins:
                diff=amt-i
                if diff<0:
                    break
                minn=min(minn,1+recal(diff))
            mem[amt]=minn
            return minn
        res=recal(amount)
        if res<float('inf'):
            return res
        else:
            return -1
