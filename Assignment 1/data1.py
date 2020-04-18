import sys
lst = [7, 2, 12, 9, 15, 4, 11, 5]
#eval(input("Input a initial list: "))



def min_max(*arr):
    if len(arr) <1:
        return ()
    mini = sys.maxsize
    maxi = -sys.maxsize-1
    for x in arr:
        if x < mini:
            mini = x
        if x > maxi:
            maxi = x
    return (mini, maxi)

def my_slice(arr, step=2):
    newList = []
    k = 1

    for i in range(len(arr)):
        if k == 1: 
            newList.append(arr[i])
        if k == step:
            k = 0
        k+=1
    return newList

def list_diff(lst, lst_b):
    return list(filter(lambda x: x not in lst_b, lst))
     
def with_factors(lst, fcts):
    def has_fcts(x, fcts):
        for fac in fcts: #[2,5]
            if x % fac == 0:
                return True
        return False
    return list(
        filter(
            lambda x:
            has_fcts(x, fcts), lst)) # [7, 2, 12, 9, 15, 4, 11, 5]

def cum_sum_pairs(lst):
    sum = 0
    newList = []
    for x in lst:
        newList.append((x,sum))
        sum +=x
    return newList

def pairs_smaller(lst):
    newList = []
    for x in lst:
        temp =[ y for y in lst if x>y]
        newList.append((x,temp))
    return newList


print('The second list of pairs as described: ', pairs_smaller(lst))
