class App:
    def __init__(self):
        self.rows: int = self.get_int("Enter row count: ")
        self.matrix: list[list[int]] = self.get_matrix(self.rows)

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

        print(matrix)

        return matrix

_ = App()