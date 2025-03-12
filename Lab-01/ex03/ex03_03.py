def tao_tuple_tu_list(n):
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    return tuple(n)

input_list = input ("Nhap vao day so cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List : ", numbers)
print(f"Tuple moi tao: {my_tuple}")