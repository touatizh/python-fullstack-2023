#1 Countdown
def countdown(x: int) -> list:
    counter = list()
    for c in range(x, -1, -1):
        counter.append(c)
    return counter
print(countdown(5)) #returns [5,4,3,2,1,0]
print("-"*3)

#2 Print and Return
def print_and_return(lst: list[int, int]) -> int:
    print(lst[0])
    return lst[1]
print(print_and_return([1,2])) #prints 1 and return 2
print("-"*3)

#3 First Plus Length
def first_plus_length(lst: list[int]) -> int:
    return lst[0]+len(lst)
print(first_plus_length([1,2,3,4,5])) #returns 6
print("-"*3)

#4 Values Greater than Second
def values_greater_than_second(lst: list[int]) -> list:
    if len(lst)<2:
        return False
    gt_lst = list()
    for item in lst:
        if item > lst[1]:
            gt_lst.append(item)
    print(len(gt_lst))
    return gt_lst
print(values_greater_than_second([5,2,3,2,1,4])) #prints 3 and returns [5,3,4]
print(values_greater_than_second([3])) #return False
print("-"*3)

#5 This Length, That Value
def length_and_value(size: int, value:int) -> list:
    lst = list()
    for i in range(size):
        lst.append(value)
    return lst
print(length_and_value(4,7)) #returns [7,7,7,7]
print(length_and_value(6,2)) #returns [2,2,2,2,2,2]