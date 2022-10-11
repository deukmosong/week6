def mean_of_n(lst):
    sum=0
    for element in lst:
        sum+=element
    
    return sum/len(lst)
   
def max_of_n(lst=[]):
    max=-9999999
    for element in lst:    
        if element>max:
            max=element
    return max
def min_of_n(lst=[]):
    min=9999999
    for element in lst:
        if min>element:
            min=element
    return min
nums= list(map(int, input().split()))

a=mean_of_n(nums)
b=max_of_n(nums)
c=min_of_n(nums)
print('평균값은 ',a)
print('최대값은 ',b)
print('최솟값은 ',c)

