// Modal add, update, delete
const modalAddPhieumuon = document.querySelector('.modal-add-phieumuon');
const modalUpdatePhieumuon = document.querySelector('.modal-update-phieumuon');
const modalDeletePhieumuon = document.querySelector('.modal-delete');
const modalConfirm = document.querySelector('.modal-trasach-phieumuon');
let thethuvienValid = false;    // Store valid thethuvien
let idThethuvien = '';          // Store id thethuvien

// Open modal add phieumuon
const open_add_phieumuon = () => {
    const modalBg = document.querySelector('.modal-bg');
    modalBg.classList.remove('d-none');
    modalAddPhieumuon.classList.remove('d-none')
}

// Close modal
const closeModalPhieumuon = () => {
    const modalBg = document.querySelector('.modal-bg');
    modalBg.classList.add('d-none');
    modalAddPhieumuon.classList.add('d-none');
    modalUpdatePhieumuon.classList.add('d-none');
    modalConfirm.classList.add('d-none');
}

function debounce(func, timeout = 300){
    let timer;
    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => { func.apply(this, args); }, timeout);
    };
}

const displayBookPhieumuon = (books, modal) => {
    const table = modal.querySelector('.table-list-book tbody');
    table.innerHTML = '';

    if (books.length > 0) {
        books.forEach(book => {
            const tr = `
                <td class="text-center align-middle">
                    <input type="radio" value="${book.name}" name="book" ${books.length == 1 ? "checked" : ""}>
                    <input type="text" class="book-quantity" value="${book.quantity}" hidden>
                </td>
                <td>${book.name}</td>
                <td>${book.author}</td>
                <td class="d-table-cell">${book.quantity}</td>
            `;
            table.innerHTML += tr;
        });
    } else {
        table.innerHTML = '<th colspan="4" class="text-center">Không có dữ liệu</th>';
    }
}

const getBooksPhieumuon = debounce((e, typeModal) => {
    // Get modal by type
    let modal = null;
    if (typeModal == 'add') {
        modal = modalAddPhieumuon;
    } else if(typeModal == 'update') {
        modal = modalUpdatePhieumuon;
    }

    if (modal == null) {
        toastr.success('Modal is null');
        return;
    }

    let name = e.target.value.trim()
    if (name == '') {
        displayBookPhieumuon([], modal);
        return;
    }

    fetch(`/getBooks_Phieumuon?name=${name}/`)
        .then(response => response.json())
        .then(data => {
            displayBookPhieumuon(data, modal);
        })
})

const searchThethuvien = (typeModal) => {
    // Get modal by type
    let modal = null;
    if (typeModal == 'add') {
        modal = modalAddPhieumuon;
    } else if (typeModal == 'update') {
        modal = modalUpdatePhieumuon;
    }
    if (modal == null) {
        toastr.error("Modal not found");
        return;
    }
    // Get id_the from input
    const id_the = modal.querySelector('.thethuvien_id').value.trim()
    if (id_the == '') {
        toastr.info("Nhập mã thẻ thư viện");
        return;
    }

    fetch(`/get_info_thethuvienById?id=${id_the}/`)
        .then(response => response.json())
        .then(data => {
            const infoDocgia = modal.querySelector('.info-docgia');
            infoDocgia.innerHTML = '';
            if (data.status == false) {
                thethuvienValid = false;
                infoDocgia.innerHTML = data.message;
            } else {
                const content = `
                    <p>Họ tên: ${data.data.hoten}</p>
                    <p>Đối tượng: ${data.data.type == 0 ? "Giảng viên" : "Sinh viên"}</p>
                    <p>Hạn thẻ: ${data.data.ngay_het_han}</p>
                    <p>Sách đang mượn:</p>
                    <ul>
                        ${data.data.books.length == 0 ? "<li>Không có</li>" : ""}
                        ${data.data.books.map(book => {
                            return `<li>${book.name} - hẹn trả: ${book.ngay_hen_tra}</li>`
                        })}
                    </ul>`;
                    
                infoDocgia.innerHTML = content;
                thethuvienValid = true;
                idThethuvien = id_the;
            }
        })
}

const searchThethuvienEnter = (event, typeModal) => {
    if (event.key === 'Enter') {
        searchThethuvien(typeModal);
    }
}

const savePhieumuon = () => {
    const bookName = modalAddPhieumuon.querySelector('input[name=book]:checked');
    if (!bookName) {
        toastr.info('Vui lòng chọn sách');
        return;
    }

    // Check quantity book
    const bookQuantity = modalAddPhieumuon.querySelector('input[name=book]:checked ~ .book-quantity');
    if (bookQuantity.value <= 0) {
        toastr.info('Số lượng sách hiện tại đã hết');
        return;
    }

    // Check validation
    if (!thethuvienValid) {
        toastr.info('Thông tin thẻ không hợp lệ');
        return;
    }

    const ghichu = modalAddPhieumuon.querySelector('.ghi-chu');
    const data = {
        'bookName': bookName.value.trim(),
        'id_the': idThethuvien,
        'ghichu': ghichu.value.trim(),
        'so_luong': 1
    }
    // Send request
    fetch('/addPhieumuonPost/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'data': JSON.stringify(data)
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.status == true) {
                toastr.success(data.message);
                setTimeout(() => {
                    location.reload();
                }, 2000)
            } else {
                toastr.error(data.message);
            }
        })
}

const deletePhieumuon = (id) => {
    const modalBg = document.querySelector('.modal-bg');
    if (modalBg && modalDeletePhieumuon) {
        modalBg.classList.remove('d-none');
        modalDeletePhieumuon.classList.remove('d-none');
        modalDeletePhieumuon.querySelector('.btn-delete').setAttribute('href', `/quan-ly-muon-tra/delete/${id}`);
    }
}

// Open modal update phieumuon
const open_update_phieumuon = (id) => {
    const modalBg = document.querySelector('.modal-bg');
    modalBg.classList.remove('d-none');
    modalUpdatePhieumuon.classList.remove('d-none');
    // Set id phieumuon
    const id_phieunhap = document.querySelector('.id-phieunhap-update');
    if (id_phieunhap) {
        id_phieunhap.value = id;
        // Get info phieumuon by id
        fetch(`/get_info_phieumuonById/${id}/`)
            .then(response => response.json())
            .then(data => {
                if (data.status == false) {
                    toastr.error(data.message);
                } else {
                    const phieumuon = data.data;
                    console.log(phieumuon);
                    // Set value to input name book
                    const nameBookInput = document.querySelector('.namebook-input');
                    nameBookInput.value = phieumuon.book.name;
                    // Display table books
                    books = [
                        phieumuon.book
                    ]
                    displayBookPhieumuon(books, modalUpdatePhieumuon);
                    // Set value to input id_thethuvien
                    const id_theInput = modalUpdatePhieumuon.querySelector('.thethuvien_id')
                    id_theInput.value = phieumuon.docgia.id_the;
                    const infoDocgia = modalUpdatePhieumuon.querySelector('.info-docgia');
                    const content = `
                        <p>Họ tên: ${phieumuon.docgia.name}</p>
                        <p>Đối tượng: ${phieumuon.docgia.type == 0 ? "Giảng viên" : "Sinh viên"}</p>
                        <p>Hạn thẻ: ${phieumuon.docgia.ngay_het_han}</p>`;
                    infoDocgia.innerHTML = content;
                    // Set value to input ghi_chu
                    const ghiChuElement = modalUpdatePhieumuon.querySelector('.ghi-chu');
                    ghiChuElement.value = phieumuon.ghi_chu;
                    // Set value to input ngay_tao, ngay_hen_tra
                    const ngay_taoElement = modalUpdatePhieumuon.querySelector('.ngay_tao');
                    ngay_taoElement.value = phieumuon.ngay_tao;
                    const ngay_hen_traElement = modalUpdatePhieumuon.querySelector('.ngay_hen_tra');
                    ngay_hen_traElement.value = phieumuon.ngay_hen_tra;
                }
            })
    }
}

// Update phieumuon
const updatePhieumuon = () => {
    // Get id phieumuon update
    const id_phieumuon = modalUpdatePhieumuon.querySelector('.id-phieunhap-update');
    if (id_phieumuon) {
        // Get data
        const bookName = modalUpdatePhieumuon.querySelector('input[name=book]:checked');
        if (!bookName) {
            toastr.info('Vui lòng chọn sách');
            return;
        }
        // Check quantity book
        const bookQuantity = modalUpdatePhieumuon.querySelector('input[name=book]:checked ~ .book-quantity');
        if (bookQuantity.value <= 0) {
            toastr.info('Số lượng sách hiện tại đã hết');
            return;
        }

        const ngay_tao = modalUpdatePhieumuon.querySelector('.ngay_tao');
        const ngay_hen_tra = modalUpdatePhieumuon.querySelector('.ngay_hen_tra');
        const ghi_chu = modalUpdatePhieumuon.querySelector('.ghi-chu');
        // Data object
        const data = {
            'id_phieumuon': id_phieumuon.value.trim(),
            'bookName': bookName.value.trim(),
            'so_luong': 1,
            'ngay_tao': ngay_tao.value,
            'ngay_hen_tra': ngay_hen_tra.value,
            'ghi_chu': ghi_chu.value.trim(),
        }
        // Fetch request to server
        fetch('/updatePhieumuonPost/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'data': JSON.stringify(data)
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.status == false) {
                    toastr.error(data.message);
                } else {
                    toastr.success(data.message);
                    setTimeout(() => {
                        window.location.reload();
                    }, 2000)
                }
            })
    }
}

// Display phieumuon
const displayPhieumuon = (phieumuons, is_showAlert) => {
    console.log(phieumuons);
    if (is_showAlert == true) {
        const alertElement = document.querySelector('.alert-search_phieumuon');
        alertElement.innerHTML = `Tìm thấy <strong>${phieumuons.length}</strong> kết quả`;
        alertElement.classList.remove('d-none');
    }
    // Show phieumuon in table
    const tablePhieumuon = document.querySelector('.table-list__phieumuon tbody');
    tablePhieumuon.innerHTML = '';
    if (phieumuons.length > 0) {
        phieumuons.forEach(pm => {
            const tr = `
                <tr>
                    <th scope="row">${pm.id_phieumuon}</th>
                    <td>${pm.bookName}</td>
                    <td>${pm.id_the}</td>
                    <td>${pm.docgiaName}</td>
                    <td>${pm.ngay_tao}</td>
                    <td>${pm.ngay_hen_tra}</td>
                    <td>${pm.trang_thai == 0 ? "Đang mượn" : ""}</td>
                    <td>${pm.so_luong}</td>
                    <td>${pm.userName}</td>
                    <td>${pm.ghichu}</td>
                    <td>
                        <button class="btn btn-outline-primary" style="margin-right: 8px" title="Sửa" onclick="open_update_phieumuon('${pm.id_phieumuon}')">
                            <i class="bi bi-gear"></i>
                        </button>
                        <button type="button" class="btn btn-outline-danger" title="Xóa" style="margin-right: 8px" onclick="deletePhieumuon('${pm.id_phieumuon}')">
                            <i class="bi bi-trash3"></i>
                        </button>
                        <button type="button" class="btn btn-outline-success" title="Xác nhận trả sách" onclick="open_modal_trasach('${pm.id_phieumuon}')">
                            <i class="bi bi-check-square"></i>
                        </button>
                    </td>
                </tr>
            `;
            tablePhieumuon.innerHTML += tr;
        });
    } else {
        tablePhieumuon.innerHTML = '<tr><th colspan="11" class="text-center">Không có dữ liệu</th></tr>';
    }
}

// Search phieumuon
const searchPhieumuon = debounce((event) => {
    let searchString = event.target.value.trim();
    let is_showAlert = true;
    if (searchString == "") {
        const alertElement = document.querySelector('.alert-search_phieumuon');
        alertElement.innerHTML = '';
        alertElement.classList.add('d-none');

        searchString = 'all';
        is_showAlert = false;
    };

    // Send request to server
    fetch(`/quan-ly-muon-tra/search-by-idThe/${searchString}`)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.status == true) {
                displayPhieumuon(data.data, is_showAlert)
            }
        })
})

// Open modal xac nhan tra sach
const open_modal_trasach = (id) => {
    // Open modal
    const modalBg = document.querySelector('.modal-bg');
    modalBg.classList.remove('d-none');
    modalConfirm.classList.remove('d-none');

    // Set id_phieumuon to input
    const idPhieumuonElement = modalConfirm.querySelector('.id_phieumuon_trasach');
    if (idPhieumuonElement) {
        idPhieumuonElement.value = id;
    }
}

// Thu hoi phieu muon
const thuhoi_phieumuon = () => {
    // Get id
    const idPhieumuon = modalConfirm.querySelector('.id_phieumuon_trasach').value;
    if (idPhieumuon == "") {
        toastr.error("Id phieumuon is empty");
        return;
    }
    // Get ghi_chu
    const ghi_chu_tra = modalConfirm.querySelector('.ghi-chu_trasach');

    data = {
        'id_phieumuon': idPhieumuon,
        'ghi_chu': ghi_chu_tra.value.trim()
    }
    // Send data to server
    fetch('/quan-ly-muon-tra/trasach/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'data': JSON.stringify(data)
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.status == true) {
                toastr.success(data.message);
                setTimeout(() => {
                    window.location.reload();
                }, 2000);
            } else {
                toastr.error(data.message);
            }
        })
        .catch(error => toastr.error(error.message))
}