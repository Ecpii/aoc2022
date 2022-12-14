from first import sizes

total_size = sizes['/']
smallest_size = 700000000
for size in sizes.values():
    if total_size - size <= 40000000:
        if size < smallest_size:
            smallest_size = size

print(smallest_size)
