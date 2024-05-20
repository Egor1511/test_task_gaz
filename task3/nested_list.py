a = [[1,2,3], [4,5,6]]

b = [{f'k{pos + 1}': num for pos, num in enumerate(item)} for item in a]

print(b)
