"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""
def matrix_multiply(arr0, arr1):
	if len(arr0) != len(arr1[0]):
		return None


	newArr = [0 in range(len(arr0[0]))][0 in range(len(arr1))]
	for x in len(arr0):
		for y in len(arr1):
			newArr[x][y] += arr0[x][y] * arr1[y][x]
	return newArr




"""
nth_largest_element

Given an input list `arr`, and index `n`, return the nth largest element.
Avoid using built-in sorting methods.
"""
def nth_largest_element(arr, n):
	max = arr[0]
	while n > 0:
		for x in arr:
			if x > max:
				max = x
		for x in range(len(arr)):
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
	for x in range(n):


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


	pass

#arr0 = [[1,2,3],[4,5,6]]
#arr1 = [[7,8],[9,10],[11, 12]]
array = [1,2,3,4,5,5,4,8]
#print(matrix_multiply(arr0, arr1))

print(nth_largest_element(array,3))