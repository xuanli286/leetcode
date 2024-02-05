def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    start_idx = 0
    end_idx = len(nums)
    while start_idx < end_idx:
        if nums[start_idx] == 0:
            nums.append(nums[start_idx])
            nums.pop(start_idx)
            if start_idx > 0:
                start_idx -= 1
            end_idx -= 1
        else:
            start_idx += 1

# Time Complexity: O(n)
# Space Complexity: O(1)

nums = [0,0,1]
moveZeroes(nums)
assert nums == [1,0,0]