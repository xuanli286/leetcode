def kidsWithCandies(candies, extraCandies):
    is_greatest =[]
    for candy in candies:
        if candy + extraCandies >= max(candies):
            is_greatest.append(True)
        else:
            is_greatest.append(False)
    return is_greatest

# Time Complexity: O(n)
# Space Complexity: O(n)

assert kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True] 