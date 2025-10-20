# write a function to remove a given word from a list ad strip it at the same time:


def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l= ["Abeer","Iram","sana","na"]
print(rem(l,"na"))


def remove_and_strip(word_list, word_to_remove):
    result = []
    for word in word_list:
        clean_word = word.strip()
        if clean_word != word_to_remove:
            result.append(clean_word)
    return result


words = [" apple ", "banana", " apple", "grape ", "orange"]
print(remove_and_strip(words, "apple"))
