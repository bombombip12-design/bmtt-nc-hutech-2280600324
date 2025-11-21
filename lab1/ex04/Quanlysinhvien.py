from Sinhvien import Sinhvien
class Quanlysinhvien:
    listSV = []
    def taoID(self):
        maxId = 1
        if (self.soluongSV() > 0):
            maxId = self.listSV[0].id
            for sv in self.listSV:
                if(maxId < sv.id):
                    maxId = sv.id
            maxId += 1
        return maxId
    def soluongSV(self):
        return self.listSV.__len__()
    
    def themSV(self):
        svId = self.taoID()
        svName = input("Nhap ten sinh vien: ")
        svSex = input("Nhap gioi tinh sinh vien: ")
        svMajor = input("Nhap chuyen nganh sinh vien: ")
        svDiemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = Sinhvien(svId, svName, svSex, svMajor, svDiemTB)
        self.xeploaihocluc(sv)
        self.listSV.append(sv)
    def capnhapSV(self, id):
        sv: Sinhvien = self.findByID(id)
        if (sv != None):
            sv.name = input("Nhap ten sinh vien: ")
            sv.sex = input("Nhap gioi tinh sinh vien: ")
            sv.major = input("Nhap chuyen nganh sinh vien: ")
            sv.diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv._name = sv.name
            sv._sex = sv.sex
            sv._major = sv.major
            sv._diemTB = sv.diemTB
            self.xeploaihocluc(sv)
        else:
            print("Khong tim thay sinh vien co ID =", format(id))
    def sapxeID(self):
        self.listSV.sort(key=lambda x: x._id, reverse = False)
    def sapxepName(self):
        self.listSV.sort(key=lambda x: x._name, reverse = False)
    def sapxepDiemTB(self):
        self.listSV.sort(key=lambda x: x._diemTB, reverse = False)
    def timID(self, id):
        searchResult = None
        if (self.soluongSV() > 0):
            for sv in self.listSV:
                if(sv.id == id):
                    searchResult = sv
            return searchResult
    def xoaID(self,keyword):
        listSinhvien = []
        if(self.soluongSV() > 0):
            for sv in self.listSV:
                if(keyword.upper() in sv._name.upper()):
                    listSinhvien.append(sv)
            return listSinhvien
    def xeploaihocluc(self, sv: Sinhvien):
        if(sv.diemTB < 5):
            sv.hocluc = "Yeu"
        elif(sv.diemTB >= 5 and sv.diemTB < 6.5):
            sv.hocluc = "Trung Binh"
        elif(sv.diemTB >= 6.5 and sv.diemTB < 7.5):
            sv.hocluc = "Kha"
        elif(sv.diemTB >= 7.5 and sv.diemTB < 9):
            sv.hocluc = "Gioi"
        else:
            sv.hocluc = "Xuat Sac"
    def showSV(self, listSinhvien):
        print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<10}".format("ID", "Ten Sinh Vien", "Gioi Tinh", "Chuyen Nganh", "Diem TB", "Hoc Luc"))
        if (listSinhvien.__len__() > 0):
            for sv in listSinhvien:
                print("{:<10} {:<20} {:<10} {:<20} {:<10} {:<10}".format(sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocluc))
        print("\n")
    def getlistSV(self):
        return self.listSV
    
        