def is_anagram(str1, str2):
    # 1. if length of string differ -> not anagram -> return False
    if len(str1) != len(str2):
        return False

    # 2. sort the letters of the strings (this is the bottle neck)
    str1 = sorted(str1)
    str2 = sorted(str2)

    # 3. and then compare the letters with the same indexes 
    for i in range(len(str1)):
        print(str1[i], 'str1')
        print(str2[i], 'str2')
        if str1[i] != str2[i]:
            return False
    return True


if __name__ == '__main__':
    s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    s2 = ['r', 'e', 's', 't', 'f', 'u', 'l']

    print(is_anagram(s1, s2))
    