def mergeAlternately(word1, word2):
    merged_str = ""
    for idx in range(min(len(word1), len(word2))):
        merged_str += word1[idx]
        merged_str += word2[idx]
    if len(word1) > len(word2):
        merged_str += word1[len(word2):]
    else:
        merged_str += word2[len(word1):]
    return merged_str
        
word1 = "abc"
word2 = "pqr"
assert mergeAlternately(word1, word2) == "apbqcr"