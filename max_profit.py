""" Problem statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ """

class Solution(object):
    def maxProfit(self, prices):
        """
        Works but overly complicated solution, reduces the amount of items to
        look at by only checking the inflection points for max profit
        """

        if len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return 0
        elif len(prices) == 2:
            if prices[1] - prices[0] > 0:
                return prices[1] - prices[0]
            else:
                return 0

        inflections = set()

        # Check if end points are inflections
        if prices[0] < prices[1]:
            inflections.add((0, prices[0]))
        if prices[len(prices)-1] < prices[len(prices)-2]:
            inflections.add((len(prices)-1, prices[len(prices)-1]))

        for i in range(2, len(prices)):
            last = prices[i-2]
            mid = prices[i-1]
            front = prices[i]
            if last >= mid and front > mid:
                inflections.add((i-1, mid))

        profits = set()
        for point in inflections:
            profits.add(max(prices[point[0]:]) - point[1])

        if profits:
            return max(profits)
        else:
            return 0

    def maxProfitSlow(self, prices):
        """
        Solution too slow, exceeds time but is correct
        """
        max_profit = 0
        if len(prices) > 0:
            min_price = prices[0]
        else:
            return max_profit

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

                check_deal = max(prices[i:]) - min_price
                if check_deal > max_profit:
                    max_profit = check_deal

        return max_profit

    def maxProfitFast(self, prices):
        """
        Fast solution, created after submitting the original solution
        """
        if len(prices) <= 1:
            return 0

        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)

        return max_profit

if __name__ == '__main__':
    s = Solution()

    print s.maxProfit([3,6])
    print s.maxProfit([7, 1, 5, 3, 6, 4])
    print s.maxProfit([7, 6, 4, 3, 1])

