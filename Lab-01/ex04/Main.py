from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien() 
while (1==1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("==================================")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim kiem sinh vien theo Ten")
    print("5. Sap xep sinh vien theo DiemTB")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")
    print("==================================")
    choice = int(input("Nhap lua chon: "))
    if (choice == 1):
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong")

    elif (choice == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("Cap nhat thong tin sinh vien")
            Id = int(input("Nhap id sinh vien can cap nhat: "))
            qlsv.updateSinhVien(Id)
        else:
            print("Danh sach sinh vien rong")

    elif (choice == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("Xoa sinh vien")
            Id = int(input("Nhap id sinh vien can xoa: "))
            if (qlsv.deleteById(Id)):
                print("Sinh vien co id = ", Id, " da bi xoa")
            else:
                print("Khong tim thay sinh vien co id = ", Id)
        else:
            print("Danh sach sinh vien rong")

    elif (choice == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("Tim kiem sinh vien theo ten")
            print("Nhap ten sinh vien can tim kiem: ")
            name = input()
            searchResult = qlsv.findbyName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien rong")
    
    elif (choice == 5):
        if(qlsv.soLuongSinhVien() > 0):
            print("Sap xep sinh vien theo diem trung binh")
            qlsv.sortByScore()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")

    elif (choice == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")

    elif (choice == 7):
        if(qlsv.soLuongSinhVien() > 0):
            print("Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")
    
    elif (choice == 0):
        break
    else:
        print("Lua chon khong hop le")
    print("==================================")