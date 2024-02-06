def productExceptSelf(nums):
    product_arr = [1] * len(nums)
    prefix = 1
    postfix = 1
    
    for preidx in range(len(nums)):
        product_arr[preidx] *= prefix
        prefix *= nums[preidx]
    for postidx in range(len(nums)-1, -1, -1):
        product_arr[postidx] *= postfix
        postfix *= nums[postidx]

    return product_arr

assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]