#This program checks whether the two input strings are anagram or not.
def anagram_check(s1,s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    index = 0
    flag = True

    while index < len(s1) and flag:
        if a_list1[index] == a_list2[index]:
            index = index + 1
        else:
            flag = False

    return flag


