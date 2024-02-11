def findMaxAverage(nums, k):
    tol = 0
    start_idx = 0
    end_idx = k
    for idx in range(0, k):
        tol += nums[idx]
    maxNum = tol
    for idx in range(k, len(nums)):
        tol -= nums[start_idx]
        tol += nums[end_idx]
        if tol > maxNum:
            maxNum = tol
        start_idx += 1
        end_idx += 1
    return maxNum / k

# Time Complexity: O(n)
# Space Complexity: O(1)

assert findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75000