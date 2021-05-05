# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
#
# Example 1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
#


# recursive solution
# def can_jump_recur(nums):
#     def can_jump(nums):
#         n = len(nums)
#         for i in range(n):
#             if i != 0:
#                 for j in range(i + 1, i + nums[i] + 1):
#                     if j == n - 1:
#                         return True
#                     if can_jump(nums[j:]):
#                         return True
#         return False
#
#     if len(nums) < 2:
#         return True
#     if nums[0] == 0:
#         return False
#     return can_jump(nums)


# recursive solution, time limit exceeded
def can_jump_recur(nums):
    if len(nums) == 1:
        return True
    for i in range(len(nums) - 2, -1, -1):
        for j in range(i, i + nums[i] + 1):
            if j == len(nums) - 1:
                if can_jump_recur(nums[:i + 1]):
                    return True
    return False


# dynamic programming solution, O(n^2) time complexity , time limit exceeded
def can_jump_dyna(nums):
    dp = [True] + [False] * (len(nums) - 1)
    for i in range(len(nums)):
        if dp[i]:
            for j in range(i, min(i + nums[i] + 1, len(nums))):
                dp[j] = True
    return dp[-1]


# O(n) time complexity
def can_jump(nums):
    lasti = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= lasti:
            lasti = i
    return lasti == 0


assert can_jump_recur([2, 3, 1, 1, 4]) is True
assert can_jump_dyna([2, 3, 1, 1, 4]) is True

assert can_jump_recur([3, 2, 1, 0, 4]) is False
assert can_jump_dyna([3, 2, 1, 0, 4]) is False

assert can_jump_recur([1]) is True
assert can_jump_dyna([1]) is True

assert can_jump_recur([0, 2, 3]) is False
assert can_jump_dyna([0, 2, 3]) is False

assert can_jump_recur([1, 0, 1, 0]) is False
assert can_jump_dyna([1, 0, 1, 0]) is False
