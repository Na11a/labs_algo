def prefix(string):
    v = [0]*len(string)
    for i in range(1, len(string)):
        k = v[i-1]
        while k > 0 and string[k] != string[i]:
            k = v[k-1]
        if string[k] == string[i]:
            k = k + 1
        v[i] = k
    return v


def kmp(string, word):
    index = -1
    prefix_array = prefix(string)
    equal_chars = 0
    for i in range(len(word)):
        while equal_chars > 0 and string[equal_chars] != word[i]:
            equal_chars = prefix_array[equal_chars-1]
            continue
        if string[equal_chars] == word[i]:
            equal_chars = equal_chars + 1
        if equal_chars == len(string):
            index = i - len(string) + 1
            break
    return index

