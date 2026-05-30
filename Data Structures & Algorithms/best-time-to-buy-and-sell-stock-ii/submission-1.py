class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(idx=0,has_stock=False):
            nonlocal dp

            if idx==len(prices):
                return 0

            if (idx,has_stock) in dp:
                return dp[(idx,has_stock)]
            
            # buy
            option1 = -math.inf
            if not has_stock:
                option1 = -prices[idx]+solve(idx+1,True)

            # sell
            option2 = -math.inf
            if has_stock:
                option2 = prices[idx]+solve(idx+1,False)
            
            # skip current idx and move ahead
            option3 = solve(idx+1,has_stock)

            dp[(idx,has_stock)] = max(option1,option2,option3)
            
            return dp[(idx,has_stock)]


        dp = dict()

        return solve()