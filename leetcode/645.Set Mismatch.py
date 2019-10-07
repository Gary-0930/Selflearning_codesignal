Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        NumWithoutRepeat = set(nums)
        RepeatNums = sum(nums) - sum(NumWithoutRepeat)
        correctNums = range(1, len(nums) + 1)
        LostNums = sum(correctNums) - sum(NumWithoutRepeat)
        return RepeatNums, LostNums
