word = 'книга'

def rearrange_pairs(word):
    rearranged_word = ""
    for i in range(0, len(word), 2):
        if i + 1 < len(word):
            rearranged_word += word[i + 1] + word[i]
        else:
            rearranged_word += word[i]
    return rearranged_word

result = rearrange_pairs(word)
print(result)
