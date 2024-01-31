def mergeAlternately(word1, word2):
    stack1 = []
    stack2 = []
    merged_str = ""
    leftover = ""
    
    if len(word2) > len(word1):
        leftover += str(word2[len(word1):])
        word2 = word2[:len(word1)]
    else:
        leftover += str(word1[len(word2):])
        word1 = word1[:len(word2)]
    
    for ch1 in word1[::-1]:
        stack1.append(ch1)
    for ch2 in word2[::-1]:
        stack2.append(ch2)
    
    while len(stack1) > 0 and len(stack2) > 0:
        merged_str += stack1.pop()
        merged_str += stack2.pop()
    merged_str += leftover
    
    return merged_str
        
word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2)) # Output: "apbqcr"