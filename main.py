# ex. 1
print("ex. 1")
list1 = [1,2,3,4,5,6,7,8,9,10]
sum1 = sum(list1)
print("The mean of the list: ", sum1 / len(list1), "\n")

# ex. 2
print("ex. 2")
list2 = [-2, -4, 5, -6, 9, 10, 1, -3, -2, 15]
list_of_pos = [e for e in list2 if e >= 0]
list_of_neg = [e for e in list2 if e < 0]

print("List of positives: ", list_of_pos)
print("List of negatives: ", list_of_neg, "\n")

# ex. 3
print("ex. 3")
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(list3)
sum3 = sum(list3[:-2])
print("The sum of the first n - 2 elements:", sum3, "\n")

# ex. 4
print("ex. 4")
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(list4)
list_of_odds = [e for i, e in enumerate(list4) if i % 2 != 0]
print("The list of odds: ", list_of_odds, "\n")

# ex. 5
print("ex. 5")
list5 = [4, 5, 2, 5, 1, 0, 32, 51, -88, 19, 1234]
list5.sort()
print("The min of the list: ", list5[0], "\n")



