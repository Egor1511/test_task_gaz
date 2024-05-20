m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

total_count, total_sum, average_value, all_in_one_tuple = (
    (sum_len := sum(len(s) for s in m),
     sum_sum := sum(sum(s) for s in m),
     sum_sum / sum_len,
     tuple(num for s in m for num in s))
)

print(f'total_count = {total_count}')
print(f'total_sum = {total_sum}')
print(f'average_value = {average_value}')
print(f'all_in_one_tuple = {all_in_one_tuple}')