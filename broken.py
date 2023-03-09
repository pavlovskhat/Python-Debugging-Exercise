def quick_sort(numbers):
   quick_sort_helper(numbers, 0, len(numbers)-1)

def quick_sort_helper(numbers, first, last):
   if first<last:

       splitpoint = partition(numbers, first, last)

       quick_sort_helper(numbers, first, splitpoint-1)
       quick_sort_helper(numbers, splitpoint+1, last)


def partition(numbers, first, last):
   pivotvalue = numbers[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and numbers[leftmark] <= pivotvalue:
           leftmark = rightmark + 1

       while numbers[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = leftmark -1

       if rightmark < leftmark -1:
           done = True
       else:
           temp = numbers[leftmark]
           numbers[leftmark] = numbers[rightmark]
           numbers[rightmark] = temp

   temp = numbers[first]
   numbers[first] = numbers[rightmark]
   numbers[rightmark] = temp

   return rightmark

numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))
