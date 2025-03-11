from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = min_product = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            print(max_product, min_product, result )
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)

        return result



print(Solution().maxProduct([3,-3,-3,3]))