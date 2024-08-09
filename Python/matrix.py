def mult_matrixes(matrix1, matrix2):
    if len(matrix1) == len(matrix2[0]):
        inverted_matrix1 = [[x,y,z] for x,y,z in zip(*original_matrix)]
        return [x+y for x, y in zip([1])]



    elif len(matrix2) == len(matrix1[0]):
        pass
    else:
        raise ValueError("Lines != columns")
    

original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

inverted_matrix = [[x,y,z] for x,y,z in zip(*original_matrix)]

print(inverted_matrix)