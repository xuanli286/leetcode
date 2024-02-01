def kidsWithCandies(candies, extraCandies):
    is_greatest = [False] * len(candies)
    max_list = []
    for idx, value in enumerate(candies):
        value1 = value + extraCandies
        if idx<=len(candies)-1 and value1 >= max(candies) and value not in max_list:
            is_greatest[idx] = True
            max_list.append(value)
        elif value in max_list:
            is_greatest[idx] = True
    return is_greatest

# Time Complexity: O(n)
# Space Complexity: O(n)

assert kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True] 