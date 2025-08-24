class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if not nums :
            return 0

        if 0 not in nums :
            return len(nums)-1
        
        if 1 not in nums :
            return 0

        if nums.count(0) == 1 :
            nums.remove(0)
            return len(nums)

        else :
            ans = 0 ; left = 0 ; zeros = 0
            for right in range(len(nums)) :
                if nums[right] == 0 :
                    zeros += 1

                while zeros > 1 :
                    if nums[left] == 0 :
                        zeros -= 1
                    left += 1

                ans = max(ans , right-left+1 - zeros)

            return ans
                    
            














                    
