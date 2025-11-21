from Quanlysinhvien import Quanlysinhvien
qlsv = Quanlysinhvien()
while(1==1):
    print("\nChuong trinh quan ly sinh vien")
    print("1. Them sinh vien")
    print("2. Cap nhap sinh vien")
    print("3. Sap xep sinh vien theo ID")
    print("4. Sap xep sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem TB")
    print("6. Tim kiem sinh vien theo ID")
    print("7. Xoa sinh vien theo ten")
    print("8. Hien thi danh sach sinh vien")
    print("9. Thoat chuong trinh")
    
    key = int(input("Nhap lua chon cua ban (1-9): "))
    if(key == 1):
        print("\nThem sinh vien")
        qlsv.themSV()
        print("Them sinh vien thanh cong!")
    elif(key == 2):
        print("\nCap nhap sinh vien")
        id = int(input("Nhap ID sinh vien can cap nhap: "))
        qlsv.capnhapSV(id)
        print("Cap nhap sinh vien thanh cong!")
    elif(key == 3):
        print("\nSap xep sinh vien theo ID")
        qlsv.sapxeID()
        qlsv.hienthiDS()
    elif(key == 4):
        print("\nSap xep sinh vien theo ten")
        qlsv.sapxepName()
        qlsv.hienthiDS()
    elif(key == 5):
        print("\nSap xep sinh vien theo diem TB")
        qlsv.sapxepDiemTB()
        qlsv.hienthiDS()
    elif(key == 6):
        print("\nTim kiem sinh vien theo ID")
        id = int(input("Nhap ID sinh vien can tim: "))
        sv = qlsv.timID(id)
        if(sv != None):
            print("Sinh vien tim thay:")
            print("ID:", sv.id, ", Ten:", sv.name, ", Gioi tinh:", sv.sex, ", Chuyen nganh:", sv.major, ", Diem TB:", sv.diemTB, ", Hoc luc:", sv.hocluc)
        else:
            print("Khong tim thay sinh vien co ID =", format(id))
    elif(key == 7):
        print("\nXoa sinh vien theo ten")
        keyword = input("Nhap ten hoac chuoi ten sinh vien can xoa: ")
        listSinhvien = qlsv.xoaID(keyword)
        if(listSinhvien.__len__() > 0):
            for sv in listSinhvien:
                qlsv.listSV.remove(sv)
            print("Da xoa", listSinhvien.__len__(), "sinh vien co ten chua chuoi '", keyword, "'")
        else:
            print("Khong tim thay sinh vien co ten chua chuoi '", keyword, "'")
    elif(key == 8):
        print("\nHien thi danh sach sinh vien")
        qlsv.hienthiDS()
    elif(key == 9):
        print("Thoat chuong trinh.")
        break