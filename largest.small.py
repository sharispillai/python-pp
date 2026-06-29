a = [100, -6, 589, 10, 2, 3, -999, 18, 23, 9]
largest = a[0]
smallest = a[0]

for i in a:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest number:", largest)
print("Smallest number:", smallest)