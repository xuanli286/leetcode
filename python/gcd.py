from math import gcd

def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    return str1[: gcd(len(str1), len(str2))]

# Time Complexity: O(logn)
# Space Complexity: O(logn)

assert gcdOfStrings("ABCABC", "ABC") == "ABC"
assert gcdOfStrings("ABABAB", "ABAB") == "AB"
assert gcdOfStrings("LEET", "CODE") == ""
assert gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX"