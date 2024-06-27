class PhieumuonDto(object):
    def __init__(self, id_phieumuon = '', ngay_tao = '', ngay_hen_tra = '',
                trang_thai = 0, ngay_tra = '', ghi_chu = '', so_luong = 0,
                id_user = '', id_sach = '', id_the = '', is_delete = 0):
        self.id_phieumuon = id_phieumuon
        self.ngay_tao = ngay_tao
        self.ngay_hen_tra = ngay_hen_tra
        self.trang_thai = trang_thai
        self.ngay_tra = ngay_tra
        self.ghi_chu = ghi_chu
        self.so_luong = so_luong
        self.id_user = id_user
        self.id_sach = id_sach
        self.id_the = id_the
        self.is_delete = is_delete