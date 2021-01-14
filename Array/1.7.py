"""Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?"""


def rotate_matrix(matrix_to_be_rotated: list):
    rotated_matrix = list()

    len_matrix = len(matrix_to_be_rotated[0])

    for each in range(0, len_matrix):
        current_row = list()
        for each1 in range(0, len_matrix):
            current_row.append(matrix_to_be_rotated[len_matrix - each1 - 1][each])
        rotated_matrix.append(current_row)
    return rotated_matrix


if __name__ == "__main__":
    print(rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
