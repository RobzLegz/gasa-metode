import numpy as np
import math

class App:
    def __init__(self):
        self.rows: int = self.get_num("Enter row count: ", integer=True)
        self.matrix: list[list[float]] = self.get_matrix(self.rows)
        self.result: list[float] = self.gauss(self.matrix)

        print("Result: ", self.result)

    def get_num(self, txt: str = "Enter int: ", integer=False) -> int:
        num = None

        while num == None:
            try:
                if integer == True:
                    num = int(input(txt))
                else:
                    num = float(input(txt))
            except:
                num = self.get_num("Try again: ")

        return num

    def get_matrix(self, rows: int) -> list[list[int]]:
        return [
            [1.17, 0.53, -0.84, 1.15],
            [0.64, -0.72, -0.43, 0.15],
            [0.32, 0.43, -0.93, -0.48]
        ]

        matrix = []

        for i in range(rows):
            row = [self.get_num(f"Enter item ({i}:{j}): ") for j in range(rows+1)]
            matrix.append(row)

        return matrix

    def floor_num(self, x: float) -> float:
        limiter = 10000
        floored = math.floor(x * limiter)

        return floored / limiter

    def gauss(self, matrix: list[list[int]]) -> list[float]:
        print("Starting matrix:")
        print(np.matrix(matrix))

        divider = matrix[0][0]

        print(f"Dividing R0 by {divider}")

        for i in range(len(matrix[0])):
            matrix[0][i] = matrix[0][i] / divider

        matrix = np.matrix(matrix)
        n = matrix.shape[0]

        print("Result matrix:")
        print(matrix)

        for i in range(n):
            pivot = matrix[i, i]
            if pivot == 0:
                raise ValueError("Can't perform Gaussian elimination: 0 pivot encountered")
            for j in range(i + 1, n):
                factor = matrix[j, i] / pivot
                print(f"{factor}R{i} + R{j}")
                matrix[j, i:] -= factor * matrix[i, i:]

                print("After elimination:")
                print(matrix)

        x = np.zeros(n)

        for i in range(n - 1, -1, -1):
            s = sum(matrix[i, j] * x[j] for j in range(i + 1, n))
            result = (matrix[i, -1] - s) / matrix[i, i]
            x[i] = self.floor_num(result)

        return x
    
_ = App()