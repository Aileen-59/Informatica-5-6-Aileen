def sum_of_row(matrix, row_number: int ):                               #expects an integer
    row = matrix[row_number]                                        #extracts the row from the matrix
    row_sum = 0                                                 #for each item of the row add it to the row
    for items in row:
        row_sum = row_sum + items
        #row_sum += items
    return row_sum


def sum_of_column(matrix, column_number: int):
    column_sum = 0                                              #initialize the sum of the column to zero
    for row in matrix:
        column_sum = column_sum + row[column_number]      #for each row in the matrix, add the item at the column index to the column sum
    return column_sum                                                       #return the column sum

m=[[4,2,3,2],[9,1,12,11],[7,8,9,5],[2,9,15,1]]                                  #4x4 matrix
# # my_sum = sum_of_row(m,1)
# my_sum = sum_of_column(m,2)                                               # sum of the 3rd column
# print(m[2][3])

def change_value(matrix, row_number, column_number, new_value):
    row = matrix[row_number]
    row[column_number] = new_value
print(m)
change_value(m,2,3,1000)
print(m)