import numpy as np

class App:
    def __init__(self):
        self.rows: int = self.get_int("Enter row count: ")
        self.matrix: list[list[int]] = self.get_matrix(self.rows)
        self.result: list[list[int]] = self.gauss(self.matrix)

        print("Rezultāts: ", self.result)

    def get_int(self, txt: str = "Enter int: ") -> int:
        num = None

        while num == None:
            try:
                num = int(input(txt))
            except:
                num = self.get_int("Try again: ")

        return num

    def get_matrix(self, rows: int) -> list[list[int]]:
        matrix = []

        for _ in range(rows):
            row = [self.get_int() for _ in range(rows+1)]
            matrix.append(row)

        return matrix

    def gauss(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        for i in range(n):
            max_row = max(range(i, n), key=lambda j: abs(matrix[j][i]))
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            for j in range(i+1, n):
                factor = matrix[j][i] / matrix[i][i]
                matrix[j][i+1:] -= factor * matrix[i][i+1:]
                matrix[j][i] = 0
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = (matrix[i][-1] - matrix[i][i+1:].dot(x[i+1:])) / matrix[i][i]
        return x

_ = App()