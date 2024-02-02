def reverseWords(s):
    s_list = s.split()
    reversed_str = " ".join(s_list[::-1])
    return reversed_str

# Time Complexity: O(n)
# Space Complexity: O(n)

assert reverseWords("the sky is blue") == "blue is sky the"
assert reverseWords("  hello world  ") == "world hello"