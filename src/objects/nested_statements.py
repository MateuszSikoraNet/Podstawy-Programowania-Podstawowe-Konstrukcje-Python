class Matrix:
    def count_even_in_matrix(self, matrix):
        # Count the even numbers in the matrix.
        pass

    def flatten(self, matrix):
        # Put all values in one list. The matrix is a list of rows (only one level of nesting).
        pass

    def transpose(self, matrix):
        # Swap the rows and columns. All rows have the same length.
        pass

    def find_pairs_with_sum(self, numbers, target):
        # Return pairs of numbers that add up to target.
        # Each pair keeps the order of the list: (earlier number, later number).
        pass

    def classify_numbers(self, numbers):
        # Group the numbers as negative, zero, or positive.
        # Return a dict with all three keys, even when a group is empty.
        pass

    def first_negative_per_row(self, matrix):
        # For each row return its first negative number, or None if the row has none.
        # break inside the inner loop leaves only the inner loop - the outer loop goes on to the next row.
        pass

    def find_in_matrix(self, matrix, target):
        # Return (row, column) of the first occurrence of target, searching row by row, or None if missing.
        # break would leave only the inner loop - use return (or a flag) to stop both loops.
        pass

    def sum_valid_numbers(self, texts):
        # Add the texts that are valid integers (int(text)) and skip the others.
        # Put try/except ValueError inside the loop, so one bad value does not stop the whole loop.
        pass
