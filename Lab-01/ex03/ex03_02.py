def dao_nguoc_list(n):
    return n[::-1]

input_list = input ("Nhap vao day so cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))

list_dao_nguoc = dao_nguoc_list(numbers)
print(f"Day so dao nguoc la: {list_dao_nguoc}")