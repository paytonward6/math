isbn_a = [3, 5, 4, 0, 9, 0, 5 ,1 ,8, 9]
isbn_a = isbn_a[::-1]

for i in range(0, 10):
    isbn_a[i] = isbn_a[i]*(i+1)
isbn_b = [0, 0, 3, 1, 1, 0, 5, 5, 9, 5]
isbn_b = isbn_b[::-1]

for i in range(0, 10):
    isbn_b[i] = isbn_b[i]*(i+1)
    
isbn_c = [0, 3, 8, 5, 4, 9 ,5 ,9 ,6 ,10]
isbn_c = isbn_c[::-1]

for i in range(0, 10):
    isbn_c[i] = isbn_c[i]*(i+1)

isbn_list = [isbn_a, isbn_b, isbn_c]
isbn_names = ['a', 'b', 'c']

for i in range(len(isbn_list)):
    isbn_sum = sum(isbn_list[i])
    print(isbn_sum)
    isbn_name = isbn_names[i]
    if isbn_sum % 11 != 0:
        print(f"{isbn_name}.) is not valid")
    else:
        print(f"{isbn_name}.) is valid")
