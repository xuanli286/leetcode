def canPlaceFlowers(flowerbed, n):
    if len(flowerbed) > 1 and len(flowerbed) >= n // 2:
        placeable_count = 0
        for idx, value in enumerate(flowerbed):
            if value == 0:
                if idx == 0 and flowerbed[idx+1] == 0:
                    placeable_count += 1
                    flowerbed[idx] = 1
                elif idx == len(flowerbed)-1 and flowerbed[idx-1] == 0:
                    placeable_count += 1
                elif flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0:
                    flowerbed[idx] = 1
                    placeable_count += 1
        if placeable_count >= n:
            return True
        return False   
    elif len(flowerbed) == 1 and (flowerbed[0] == 0 and n<=1) or (flowerbed[0] == 1 and n==0):
        return True
    return False

# Time Complexity: O(n)
# Space Complexity: O(1)

assert canPlaceFlowers([1,0,0,0,1], 1) == True
assert canPlaceFlowers([1,0,0,0,1], 2) == False
assert canPlaceFlowers([1,0,0,0,0,0,1], 2) == True