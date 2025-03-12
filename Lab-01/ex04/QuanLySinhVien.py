from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []

    def generateId(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id 
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId += 1
        return maxId
    
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def nhapSinhVien(self):
        svId = self.generateId()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap nganh hoc: ")
        score = float(input("Nhap diem: "))
        sv = SinhVien(svId, name, sex, major, score)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, Id):
        sv: SinhVien = self.findbyID(Id)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh: ")
            major = input("Nhap nganh hoc: ")
            score = float(input("Nhap diem: "))
            sv._name = name
            sv.sex = sex
            sv.major = major
            sv.score = score
            self.xepLoaiHocLuc(sv)
        else:
            print("Khong tim thay sinh vien co id = ", Id)

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
    
    def sortByScore(self):
        self.listSinhVien.sort(key=lambda x: x._score, reverse=False)
    
    def findbyID(self, Id):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == Id):
                    searchResult = sv
        return searchResult
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    
    def deleteById(self, Id):
        isDeleted = False
        sv = self.findbyID(Id)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._score >= 8):
            sv._rank = "Gioi"
        elif (sv._score >= 6.5):
            sv._rank = "Kha"
        elif (sv._score >= 5):
            sv._rank = "Trung binh"
        else:
            sv._rank = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Score", "Rank"))

        if(listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._score, sv._rank))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien