tuple1 = tuple(map(int, input().split()))
tuple2 = tuple(map(int, input().split()))
combined_tuple = tuple1 + tuple2
sorted_values = tuple(sorted(combined_tuple))
print(combined_tuple)
print(sorted_values)