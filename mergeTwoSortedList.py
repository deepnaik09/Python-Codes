class Solution:
    def mergeList(list1, list2):
        list3 = []
        for i in range(((len(list1)+len(list2))//2)-1):
            if list1[i]>=list2[i]:
                temp = list1[i]
                list1[i] = list2[i]
                list2[i] = temp
