"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""


def matrix_multiply(arr0, arr1):
    if len(arr0) != len(arr1[0]):
        return None
    newArr = [[0 for col in range(len(arr0))] for row in range(len(arr1[0]))]
    for x in range(len(arr0)):
        for y in range(len(arr1[0])):
            for z in range(len(arr1)):
                newArr[x][y] += arr0[x][z] * arr1[z][y]
    return newArr


"""
nth_largest_element

Given an input list `arr`, and index `n`, return the nth largest element.
Avoid using built-in sorting methods.
"""


def nth_largest_element(arr, n):
    if n <= 0:
        return None
    if arr == None:
        return None
    if n > len(arr):
        return None
    while n > 0:
        max = arr[0]
        for x in arr:
            if x > max:
                max = x
        for x in range(arr.count(max)):
            arr.remove(max)
        n -= 1
    return max


"""
reverse_block

Given an input list `arr`, and a block size `n` > 0, reverse the list in blocks of n.

Example:
	Arguments:
		[1,2,3, 4,5,6, 7], 3
	Return:
		[3,2,1, 6,5,4, 7]
	(spacing added for emphasis)

"""


def reverse_block(arr, n):
    print(arr)
    newArr = []
    count = 0;
    for x in range(int(len(arr) / n)):
        print(int(len(arr) / n), x)
        tempArr = []
        for y in range(n):
            print(y, count, arr[y + count])
            tempArr.append(arr[y + count])
        tempArr.reverse()
        for num in tempArr:
            newArr.append(num)
        count += n
    tempArr = []
    for x in range(len(arr) % n):
        print(arr[len(arr) - x - 1])
        tempArr.append(arr[len(arr) - x - 1])
    for num in tempArr:
        newArr.append(num)
    return newArr


"""
subset_sum

Given an input list `arr`, and a number `target`, return whether or not any possible subset of the values in `arr` could sum to `target`.

Example 1:
	Arguments:
		[1,2,3,4,5,7], 13
		7 + 4 + 2 = 13
	Return:
		True

Example 2:
	Arguments:
		[1,2,-1,5,4,-196], 196
	Return:
		False
"""


def subset_sum(arr, target):
    pass


"""
spiral_matrix

Given an input 2-D array, return a list with the values obtained by following a clockwise spiral path, starting from [0][0], then proceeding to [0][n], [m][n], [m][0], then going inwards:

Example:
	Argument:
		[[a,b,c,d,e],
		 [f,g,h,i,j],
		 [k,l,m,n,o],
		 [p,q,r,s,t],
		 [u,v,w,x,y]]
	Return:
		[a,b,c,d,e, j,o,t,y, x,w,v,u, p,k,f, g,h,i, n,s, r,q, l, m]
"""


def spiral_matrix(arr):
    if arr == None:
        return None

    newArr = []

    while len(arr) != 0:
        for col in range(len(arr[0])):
            newArr.append(arr[0].pop(0))

        if len(arr) == 0:
            return newArr
        del arr[0]
        for row in range(len(arr)):
            newArr.append(arr[row].pop())

        if len(arr) == 0:
            return newArr
        for bottomCols in range(len(arr)):
            newArr.append(arr[len(arr[0]) - 1].pop())

        if len(arr) == 0:
            return newArr
        del arr[len(arr[0]) - 1]
        for leftRow in range(1, len(arr[0])):
            newArr.append(arr[len(arr) - leftRow].pop(0))


arr0 = [[1, 2, 3], [4, 5, 6]]
arr1 = [[7, 8], [9, 10], [11, 12]]
array = [1, 2, 3, 4, 5, 5, 4, 8, 10, 12, 13]
test = [[1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]]
print(spiral_matrix(test))

# print(len(array) % 4)
