"""Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
make a function for it"""

def find_odd_repeatation(array)->int:
    counter = 0
    result = {}
    if len(array)==1:
        return array[0]
    elif len(array)>1:
        for i in array:
            for j in array:
                if i == j:
                    counter+=1
            if counter%2 ==1:
                result[f'test{i}'] = i
            counter = 0
        return result.values()
                


test = [1,2,2,3,3,3,4,3,3,3,2,2,1,1]
test_1 = [0,1,0,1,0]
test_2 = [1,1,2]
print(find_odd_repeatation(test_2))

            


# "odd and even"
# test = 2 %2
# print(test)
