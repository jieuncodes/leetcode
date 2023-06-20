# sliding window
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        x = 2*k +1
        tmp = sum(nums[:(k*2)+1])

        for i,num in enumerate(nums):
            if i < k:
               res.append(-1)
            elif i >= len(nums) - k:
                res.append(-1)
            elif i == k:
                res.append(int(tmp/x))
            else:
                tmp += nums[i+k] - nums[i-k-1]
                res.append(int(tmp/x))
        return res
            


# Other solutions - better to set default arr values first
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        windowSize = 2 * k + 1
        ans = [-1] * n
        
        if n < windowSize:
            return ans
        
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        for i in range(k, n - k):
            ans[i] = (prefixSum[i + k + 1] - prefixSum[i - k]) // windowSize
        
        return ans
    

# my optimized solution
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        windowSize = 2 * k + 1
        res = [-1] * n

        if n < windowSize:
            return res

        tmp = sum(nums[:windowSize]) if n >= windowSize else sum(nums)

        for i in range(k, n - k):
            res[i] = tmp // windowSize
            if i + k + 1 < n:
                tmp = tmp - nums[i - k] + nums[i + k + 1]

        return res
