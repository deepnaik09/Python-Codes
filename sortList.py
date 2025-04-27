class Solution:
    def sortList(list1):
        print(list1)
        for i in range(len(list1)):
             for j in range(i+1, len(list1)):
                if list1[i] >= list1[j] :
                    temp = list1[i]
                    list1[i] = list1[j]
                    list1[j] = temp
                    
        print(list1)
    list1 = [5, 3, 0, 2, 4, 9, 6, 7, 2, 1]
    sortList(list1)
   
