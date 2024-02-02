def reverseVowels(s):
    vowel_stack = []
    reversed_str = ""

    for ch in s:
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_stack.append(ch)
    
    for ch in s:
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            reversed_str += vowel_stack.pop()
        else:
            reversed_str += ch
    
    return reversed_str

# Time Complexity: O(n)
# Space Complexity: O(n)

assert reverseVowels("hello") == "holle"
assert reverseVowels("leetcode") == "leotcede"