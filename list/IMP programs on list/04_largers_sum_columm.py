def largest_sum_column(li):
    m = len(li)
    n = len(li[0])

    max_sum = -1
    max_sum_column = -1

    for column_no in range(n):
        sum = 0
        for row_no in range(m):
            sum+=li[row_no][column_no]
        if(sum > max_sum) :
            max_sum = sum
            max_sum_column = column_no

    return max_sum,max_sum_column

li = [[1,2,3,4],[8,7,6,5],[9,10,11,7]]
lar_sum, lar_column = largest_sum_column(li)  
print(lar_column,lar_sum)