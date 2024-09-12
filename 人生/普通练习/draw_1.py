def canPermutePalindrome(self, s: str) -> bool:
    l = len(s)
    l_set = len(set(s))
    if l // 2 == l_set + 1 or l // 2 == l_set:
        return True
    else:
        return False


