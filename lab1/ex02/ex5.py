so_gio_lam = float(input("Nhap so gio lam: "))
luong_mot_gio = float(input("Nhap luong mot gio: "))
gio_tieu_chuan = 40
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
luong = (so_gio_lam * luong_mot_gio) + (gio_vuot_chuan * luong_mot_gio * 1.5)
print("Tong luong nhan duoc la:", luong)