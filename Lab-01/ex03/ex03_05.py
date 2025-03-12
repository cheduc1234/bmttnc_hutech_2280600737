def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for i    in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

input_list = input("Nhap vao day so cach nhau boi dau phay: ")
word_list = input_list.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua moi phan tu la: ", so_lan_xuat_hien)