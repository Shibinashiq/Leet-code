class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if k <= 0:
            return False

        num_set = set()

        for i in range(len(nums)):
            if nums[i] in num_set:
                return True

            num_set.add(nums[i])

            if len(num_set) > k:
                num_set.remove(nums[i - k])

        return False

        