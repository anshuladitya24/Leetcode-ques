class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        if n != 1:
            for i in range(n):
                if nums[i] in freq:
                    freq[nums[i]] += 1

                    if freq[nums[i]] > n/2:
                        return nums[i]
                else:
                    freq[nums[i]] = 1

        else:
            return nums[0]

