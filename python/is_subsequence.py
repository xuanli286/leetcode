def isSubsequence(s, t):
    stack_s = []
    idx_t = len(t)-1

    for idx_s in range(len(s)-1, -1, -1):
        stack_s.append(s[idx_s])

    while len(stack_s) > 0 and idx_t >= 0:
        if t[idx_t] == stack_s[0]:
            stack_s.pop(0)
        idx_t -= 1

    if len(stack_s) == 0:
        return True
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)

assert isSubsequence("abc", "ahbgdc") == True
assert isSubsequence("axc", "ahbgdc") == False
