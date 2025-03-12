def chia_het_cho_5(so_nhi_phan):
   
    so_thap_phan = int(so_nhi_phan, 2)
    
    
    return so_thap_phan % 5 == 0


so_nhi_phan_list = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ").split(",")


so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]


if len(so_chia_het_cho_5) > 0:
    print("Các số nhị phân chia hết cho 5 là:", ",".join(so_chia_het_cho_5))
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")