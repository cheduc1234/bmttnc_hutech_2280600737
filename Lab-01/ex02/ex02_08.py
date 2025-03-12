def chia_het_cho_5(so_nhi_phan):  
    # Chuyển số nhị phân sang số thập phân  
    try:  
        so_thap_phan = int(so_nhi_phan, 2)  
    except ValueError:  
        # Nếu chuỗi không phải là số nhị phân hợp lệ  
        return False  
    
    # Kiểm tra xem số thập phân có chia hết cho 5 không  
    return so_thap_phan % 5 == 0  

# Nhập chuỗi số nhị phân từ người dùng  
so_nhi_phan_list = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ").split(",")  

# Lọc những số nhị phân chia hết cho 5  
so_chia_het_cho_5 = [so.strip() for so in so_nhi_phan_list if chia_het_cho_5(so.strip())]  

# In kết quả  
if len(so_chia_het_cho_5) > 0:  
    print("Các số nhị phân chia hết cho 5 là:", ", ".join(so_chia_het_cho_5))  
else:  
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")