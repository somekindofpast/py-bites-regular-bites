class Matrix:

    def __init__(self, values: list[list[int]]):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        return Matrix(matmul(self.values, other.values))

    def __rmatmul__ (self, other):
        return Matrix(matmul(self.values, other.values))

    def __imatmul__ (self, other):
        self.values = matmul(self.values, other.values)
        return self


def matmul(val_a: list[list[int]], val_b: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range(len(val_a)):
        res.append([])

        for k in range(len(val_b)):
            mult = 0
            for j in range(len(val_a[i])):
                mult += val_a[i][j] * val_b[j][k]
            res[-1].append(mult)

    return res


if __name__ == '__main__':
    class MatrixWithoutMatMul:

        def __init__(self, values):
            self.values = values
            self.col = len(values[0])
            self.row = len(values)

        def __matmul__(self, other):
            return NotImplemented

    print("matmul test:")
    mat1 = Matrix([[1, 2],  [3, 4]])
    mat2 = Matrix([[11, 12], [13, 14]])
    print(mat1 @ mat2)
    print(mat2 @ mat1)

    print("\nrmatmul test:")
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = MatrixWithoutMatMul([[11, 12], [13, 14]])
    print(mat2 @ mat1)
