# Given an integer array nums, return true if any value appears a least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: False

# Example 3:
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: True

# firts solution
# O(n^2) where n is the size of the input array - this is the brute force method
# good thing is no extra memory is needed

# second soluiton
# sorting - if we sort then any duplicates that do exist, will be adjacent, meaning just checking the neighbours and then shift pointers to the next spot until the array is finished
# time complexity is O but sorting does take more time complexity and more memory but no extra space will be used --> O(nlogn)

# if we don't sort our input, we're given the default input but we use extra memory, we use a hashset. 
# What is a hashset? it will allow us to insert elements into a hashset in big O(1) and also allow us to check. Does a certain value exist, so 1 does not exist hence it is not a duplicate,
# time complexity is O(n) but does take more space as it will take up the size of the array in the hashset O(n)

# code

class Solution:
    def constainsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

        