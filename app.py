import numpy as np

class App:
    def __init__(self):
        self.rows: int = self.get_int("Enter row count: ")
        self.matrix: list[list[int]] = self.get_matrix(self.rows)
        self.result: list[list[int]] = self.gauss(self.matrix)

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
            row = []

            for _ in range(rows + 1):
                item = self.get_int()

                row.append(item)

            matrix.append(row)

        return matrix

    def gauss(self, matrix: list[list[int]]) -> list[int]:
        vector = [item[len(item) - 1] for item in matrix]
        matrix = [item.pop() for item in matrix]

        print(vector)
        print(matrix)

        n = len(matrix)
        for i in range(n):
            max_row = i
            for j in range(i+1, n):
                if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                    max_row = j
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            vector[i], vector[max_row] = vector[max_row], vector[i]
            for j in range(i+1, n):
                factor = matrix[j][i]/matrix[i][i]
                for k in range(i+1, n):
                    matrix[j][k] -= factor*matrix[i][k]
                vector[j] -= factor*vector[i]
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            s = sum(matrix[i][j]*x[j] for j in range(i+1, n))
            x[i] = (vector[i] - s)/matrix[i][i]
        return x

_ = App()