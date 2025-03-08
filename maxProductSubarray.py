class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #this is a dp problem
        res = max(nums)
        minProd, maxProd = 1,1
        for n in nums:
            if n == 0:
                minProd, maxProd = 1,1
            tmp = n * maxProd
            maxProd = max(n, tmp, n * minProd)
            minProd = min(n, tmp, n * minProd)
            res = max(res, maxProd)
        return res