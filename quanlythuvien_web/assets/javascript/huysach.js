
// Get element phieuhuy
const bookCategoryPhieuhuy = document.getElementById('bookCategory');
const bookAuthorPhieuhuy = document.getElementById('bookAuthor');
const bookQuantityCurrPhieuhuy = document.getElementById('bookQuantityCurrent');
const bookQuantityPhieuhuy = document.getElementById('bookQuantity');
const lydoPhieuhuy = document.querySelector('.ly-do_huysach');
const bookSelectPhieuhuy = document.getElementById('bookSelect');

let booksPhieuhuy = [];
let ctph_deletes = [];
let bookNamePhieuhuy = '';
let id_sachPhieuhuy = '';

const resetInputPhieuhuy = () => {
    bookSelectPhieuhuy.value = '0';
    bookCategoryPhieuhuy.value = '';
    bookAuthorPhieuhuy.value = '';
    bookQuantityCurrPhieuhuy.value = '';
    bookQuantityPhieuhuy.value = '';
    lydoPhieuhuy.value = '';
}

// Handle listen event change select
const chooseBookPhieuhuy = (element) => {
    id_sachPhieuhuy = '';
    const id_book = element.value;
    if (id_book !== '0') {
        console.log(id_book);
        fetch(`/getBookById?id=${id_book}/`)
            .then(response => response.json())
            .then(data => {
                if (data.status == true) {
                    console.log(data);
                    bookNamePhieuhuy = data.data.name;
                    bookCategoryPhieuhuy.value = data.data.nameCategory;
                    bookAuthorPhieuhuy.value = data.data.author;
                    bookQuantityCurrPhieuhuy.value = data.data.quantity;
                    bookQuantityPhieuhuy.value = '';
                    lydoPhieuhuy.value = '';
                } else {
                    toastr.error(data.message);
                }
            })
    } else {
        // Reset value input
        resetInputPhieuhuy();
    }
}

// Display list book
const displayBooksPhieuhuy = (books) => {
    const table = document.querySelector('.table-books_phieuhuy tbody');
    if (table) {
        table.innerHTML = '';
        if (books.length > 0) {
            let stt = 1;
            books.forEach(book => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <th>${stt}</th>
                    <td>${book.name}</td>
                    <td>${book.category}</td>
                    <td>${book.author}</td>
                    <td>${book.quantity}</td>
                    <td>${book.note}</td>
                    <td class="align-middle d-table-cell">
                        <button type="button" class="btn btn-outline-primary" onclick="handleUpdateBookPhieuhuy('${book.id_ctph}')" style="margin-right: 8px" title="Sửa">
                            <i class="bi bi-gear"></i>
                        </button>
                        <button type="button" class="btn btn-outline-danger" onclick="deleteBookPhieuhuy('${book.id_ctph}')" style="margin-right: 8px" title="Sửa">
                            <i class="bi bi-trash3"></i>
                        </button>
                    </td>
                `;
                table.appendChild(tr);
                stt++;
            });
        } else {
            table.innerHTML = '<tr><th colspan="7">Không có sách nào</th></tr>';
        }
    } else {
        console.log('Table not found');
    }
}

// Handle validation quantity & lydo huy sach
const validationPhieuHuy = () => {
    let quantity = bookQuantityPhieuhuy.value.trim();
    let lydo = lydoPhieuhuy.value.trim();
    if (quantity == '') {
        toastr.info('Vui lòng nhập số lượng hủy');
        bookQuantityPhieuhuy.focus();
        return false;
    } else if (parseInt(quantity) <= 0) {
        toastr.info('Số lượng hủy phải lớn hơn 0');
        bookQuantityPhieuhuy.focus();
        return false;
    } else if (parseInt(quantity) > parseInt(bookQuantityCurrPhieuhuy.value)) {
        toastr.info('Số lượng hủy không được lớn hơn số sách hiện có');
        bookQuantityPhieuhuy.focus();
        return false;
    }
    if (lydo == '') {
        toastr.info('Vui lòng nhập lý do hủy');
        lydoPhieuhuy.focus();
        return false;
    }
    return true;
}

// Add book to ct phieuhuy
const addBookPhieuHuy = () => {
    // Check validation
    if (bookSelectPhieuhuy.value == "0") {
        bookSelectPhieuhuy.focus();
        toastr.info('Vui lòng chọn sách muốn hủy');
        return;
    }
    // Check book exist by id
    const book = booksPhieuhuy.find(book => book.id_sach === bookSelectPhieuhuy.value);
    if (book) {
        toastr.info('Sách này đã có trong phiếu hủy');
        return;
    }

    if (validationPhieuHuy()) {
        // Add book to list
        const book = {
            'id_ctph': (booksPhieuhuy.length + 1).toString(),
            'id_sach': bookSelectPhieuhuy.value,
            'name': bookNamePhieuhuy,
            'category': bookCategoryPhieuhuy.value,
            'author': bookAuthorPhieuhuy.value,
            'quantity': bookQuantityPhieuhuy.value.trim(),
            'quantityCurr': bookQuantityCurrPhieuhuy.value,
            'note': lydoPhieuhuy.value.trim()
        }
        booksPhieuhuy.push(book);
        displayBooksPhieuhuy(booksPhieuhuy);
        resetInputPhieuhuy();
    }
}

// Handle get value book update
const handleUpdateBookPhieuhuy = (id) => {
    const book = booksPhieuhuy.find((item) => item.id_ctph === id);
    if (!book) {
        toastr.error('Book not found');
        return;
    } else {
        // Get options book
        const options = bookSelectPhieuhuy.querySelectorAll('option');
        options.forEach(option => {
            if (option.value === book.id_sach) {
                bookSelectPhieuhuy.value = book.id_sach;
            }
        })
        // Set value book
        id_sachPhieuhuy = book.id_sach;
        bookCategoryPhieuhuy.value = book.category;
        bookAuthorPhieuhuy.value = book.author;
        bookQuantityCurrPhieuhuy.value = book.quantityCurr;
        bookQuantityPhieuhuy.value = book.quantity;
        lydoPhieuhuy.value = book.note;
    }
}

// Update book ct phieuhuy
const updateBookPhieuHuy = () => {
    if (id_sachPhieuhuy == '') {
        toastr.info('Chọn sách muốn cập nhật');
        return;
    }
    if (validationPhieuHuy()) {
        const book = booksPhieuhuy.find(book => book.id_sach === id_sachPhieuhuy);
        if (book) {
            book.quantity = bookQuantityPhieuhuy.value.trim();
            book.note = lydoPhieuhuy.value.trim();
            displayBooksPhieuhuy(booksPhieuhuy);
            resetInputPhieuhuy();
        } else {
            toastr.error('Book not found');
        }
    }
}

// Delete book to ct phieuhuy
const deleteBookPhieuhuy = (id) => {
    booksPhieuhuy = booksPhieuhuy.filter(book => book.id_ctph !== id);
    ctph_deletes.push(id);
    displayBooksPhieuhuy(booksPhieuhuy);
}

// Submit form huysach to serverr
const submitAddPhieuhuy = (event) => {
    event.preventDefault();
    if (booksPhieuhuy.length > 0) {
        const data = {
            'books': booksPhieuhuy
        }

        // Send request to server
        fetch('/huysachPost/', {
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
                        window.location.href = '/quan-ly-kho-sach/huy-sach/';
                    }, 2000);
                } else {
                    toastr.error(data.message);
                }
            })
        } else {
        toastr.info('Thông tin sách hủy đang trống');
    }
}

// Submit form update phieuhuy
const submitUpdatePhieuhuy = (event) => {
    event.preventDefault();
    if (booksPhieuhuy.length > 0) {
        const id_phieuhuy = document.querySelector('.phieuhuy-id').value;
        const ngay_huy = document.querySelector('.ngayhuy').value;

        const data = {
            'id_phieuhuy': id_phieuhuy,
            'ngay_huy': ngay_huy,
            'books': booksPhieuhuy,
            'ctph_deletes': ctph_deletes
        }

        // Send request to server
        fetch('/updatePhieuhuyPost/', {
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
                        window.location.href = '/quan-ly-kho-sach/huy-sach/';
                    }, 2000);
                } else {
                    toastr.error(data.message);
                }
            })
        } else {
        toastr.info('Thông tin sách hủy đang trống');
    }
}

// Delete phieuhuy
const deletePhieuhuy = (id) => {
    const modalBg = document.querySelector('.modal-bg');
    const modalDelete = document.querySelector('.modal-delete');
    modalBg.classList.remove('d-none');
    modalDelete.classList.remove('d-none');
    modalDelete.querySelector('.btn-delete').setAttribute('href', `/quan-ly-kho-sach/huy-sach/delete/${id}`);
}

// Search phieuhuy
const searchPhieuhuyByDate = () => {
    const dateFrom = document.querySelector('#search-date-from').value.trim();
    const dateTo = document.querySelector('#search-date-to').value.trim();

    if (!dateFrom || !dateTo) {
        toastr.info('Vui lòng chọn ngày bắt đầu và ngày kết thúc');
        return;
    }
    window.location.href = `/quan-ly-kho-sach/huy-sach/search/${dateFrom}/${dateTo}`;
}

displayBooksPhieuhuy(booksPhieuhuy);