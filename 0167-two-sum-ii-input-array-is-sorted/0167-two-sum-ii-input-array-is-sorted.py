class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Two-pointer approach (O(n) time, O(1) space) since array is sorted
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            # If sum matches target, return 1-based indices
            if current_sum == target:
                return [left + 1, right + 1]
            # If sum is too small, move left pointer right
            elif current_sum < target:
                left += 1
            # If sum is too large, move right pointer left
            else:
                right -= 1
        
        # Problem guarantees exactly one valid solution exists
        # So this return is just for static analysis (won't be reached)
        return [-1, -1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna