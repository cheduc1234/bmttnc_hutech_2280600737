def tinh_tong_so_chan(n):
    tong = 0 
    for num in n:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input ("Nhap vao day so cach nhau boi dau phay: ") 
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print(f"Tong cac so chan trong day so la: {tong_chan}")