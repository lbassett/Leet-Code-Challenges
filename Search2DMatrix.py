# Search 2D Matrix
# Efficiently determine if an element is in a 2D matrix, given that the matrix rows are sorted
# in ascending order, and the first element of a row is greater than or equal to the last element
# of the previous row


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    
    numrows = len(matrix)
    if numrows == 0:
        return(False)
    elif len(matrix[0]) == 0:
        return(False)
    elif matrix[0][0] > target:
        return(False)
    else:
        index = 1
        searchrow = None
        while index < numrows:
            if matrix[index][0] > target:
                searchrow = index -1
                break
            index += 1
        if searchrow == None:
            searchrow = index -1
        
        row = matrix[searchrow]
        return(target in row)

# Time Complexity: For an m x n matrix, O(m+n)
# Space Complexity: O(1)
