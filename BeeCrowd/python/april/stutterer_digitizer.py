def remove_stutterings(word_list):
    return ' '.join([word.replace(word[:2],'',1) if word[:2] == word[2:4] else word for word in word_list])

stuttering = input().split()
print(remove_stutterings(stuttering))