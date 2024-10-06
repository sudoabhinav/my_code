"""
Problem statement link
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_mapping = dict()
        result = list()
        for index, val in enumerate(nums):
            try:
                nums_mapping[val].append(index)
            except:
                nums_mapping[val] = list()
                nums_mapping[val].append(index)
        flag = 0
        for key, value in nums_mapping.items():
            diff_val = target - key
            if nums_mapping.get(diff_val) and (diff_val != key or len(nums_mapping.get(diff_val)) > 1):
                if len(nums_mapping.get(diff_val)) > 1:
                    result = nums_mapping.get(diff_val)
                else:
                    result.append(value[0])
                    result.append(nums_mapping.get(diff_val)[0])
                flag = 1
            if flag == 1:
                break
        return result


        