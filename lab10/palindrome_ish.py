def almost_palindrome(word, k):
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        if k == 0:
            return False
        else:
            return almost_palindrome(word[1:], k - 1) or almost_palindrome(word[:-1], k - 1)
    else:
        return almost_palindrome(word[1:-1], k)


res = almost_palindrome(input(), int(input()))

if res:
    print("sim")
else:
    print("nao")
