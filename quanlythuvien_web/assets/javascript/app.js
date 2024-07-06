// Handle active sidebar
const pathnameCurrent = window.location.pathname.toLowerCase().split('/');

// Add class active vào thẻ link navbar
const navLinks = document.querySelectorAll('.sidebar .sidebar-link');
navLinks.forEach(navLink => {
    // console.log(navLink.getAttribute('page').toLowerCase());
    // Get value attribute id
    const valueAttId = navLink.getAttribute('page').toLowerCase();
    if (pathnameCurrent.includes(valueAttId)) {
        navLink.classList.add('active');
    } else {
        navLink.classList.remove('active');
    }
})

// Image upload to cloudinary
async function uploadImage(file, folderName) {
    const cloudName = 'dvtvl2un6';
    const unsignedUploadPreset = 'sqsfjomd';
    const url = `https://api.cloudinary.com/v1_1/${cloudName}/upload`;

    const fd = new FormData();
    fd.append('folder', folderName);
    fd.append('upload_preset', unsignedUploadPreset);
    fd.append('tags', 'browser_upload'); // Optional - add tags for image admin in Cloudinary
    fd.append('file', file);

    const response = await fetch(url, {
        method: 'POST',
        body: fd,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
    });

    return response.json();
}

// Lap phieu nhap variables
let listBooks = [];
let list_bookDelete = [];
let id_book = '';
let bookSelect = document.querySelector('.book-select');
let bookName = document.querySelector('.book-name');
let bookAthor = document.querySelector('.book-author');
let bookPrice = document.querySelector('.book-price');
let bookQuantity = document.querySelector('.book-quantity');
let bookCategory = document.querySelector('.book-category');

// Handle add book in lap phieu nhap
const addBookPhieuNhap = async () => {
    // Check value input
    if (!bookName.value || !bookAthor.value || !bookPrice.value || !bookQuantity.value || !bookCategory.value) {
        alert('Vui lòng nhập đầy đủ thông tin sách');
        return;
    }

    // Check book exist
    const is_book = listBooks.find(book => book.name === bookName.value.trim());
    if (is_book) {
        toastr.error('Sách đã tồn tại')
        return;
    }

    // If not choose image set image default
    // if (!bookImage.files[0]) {
    //     bookImageSrc = 'https://plus.unsplash.com/premium_photo-1667251760532-85310936c89a?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D';
    // } else {
    //     // Upload image to cloudinary
    //     const image = await uploadImage(bookImage.files[0], `quanlythuvien/book`);
    //     bookImageSrc = image.secure_url;
    // }

    // Add book to list
    const book = {
        id: (listBooks.length + 1).toString(),
        name: bookName.value.trim(),
        author: bookAthor.value.trim(),
        price: bookPrice.value.trim(),
        quantity: bookQuantity.value.trim(),
        category: {
            id: bookCategory.value,
            name: bookCategory.options[bookCategory.selectedIndex].text
        },
    }

    listBooks.push(book);
    displayBook(listBooks);

    // Reset value input
    bookName.value = '';
    bookAthor.value = '';
    bookPrice.value = '';
    bookQuantity.value = '';
    bookCategory.selectedIndex = 0;
    bookSelect.selectedIndex = 0;
    bookName.disabled = false;
    bookAthor.disabled = false;
    bookCategory.disabled = false;
}

// Update book
const updateBookPhieuNhap = async () => {
    // If have id book
    if (id_book !== '') {
        const book = listBooks.find(book => book.id === id_book);
        if (!book) return;

        // Get value input
        book.name = bookName.value.trim();
        book.author = bookAthor.value.trim();
        book.price = bookPrice.value.trim();
        book.quantity = bookQuantity.value.trim();
        book.category = {
            id: bookCategory.value,
            name: bookCategory.options[bookCategory.selectedIndex].text
        }

        // Handle image if choose image change new image
        // if (bookImage.files[0]) {
        //     // Upload image to cloudinary
        //     const image = await uploadImage(bookImage.files[0], `quanlythuvien/book`);
        //     book.image = image.secure_url;
        // }

        // Display book
        displayBook(listBooks);

        // Reset value input
        id_book = '';
        bookName.value = '';
        bookAthor.value = '';
        bookPrice.value = '';
        bookQuantity.value = '';
        bookCategory.selectedIndex = 0;
    }
}

// Handle update book set value input in lap phieu nhap
const handleUpdateBook = (id) => {
    const book = listBooks.find(book => book.id === id);
    if (!book) return;

    // Set id book
    id_book = book.id;

    // Get option category
    const options = bookCategory.querySelectorAll('option');
    options.forEach(option => {
        if (book.category.id === option.value) {
            option.selected = true;
        }
    });

    // Set value input
    bookName.value = book.name;
    bookAthor.value = book.author;
    bookPrice.value = book.price;
    bookQuantity.value = book.quantity;

    // Select book if exist in list
    const optionsBook = bookSelect.querySelectorAll('option');
    let isBook = false;
    optionsBook.forEach(option => {
        if (book.name === option.text) {
            option.selected = true;
            isBook = true;
        }
    })

    if (isBook) {
        bookName.disabled = true;
        bookAthor.disabled = true;
        bookCategory.disabled = true;
    } else {
        optionsBook[0].selected = true;
        bookName.disabled = false;
        bookAthor.disabled = false;
        bookCategory.disabled = false;
    }
}

// Handle delete book in lap phieu nhap
const handleDeleteBook = (id) => {
    listBooks = listBooks.filter(book => book.id !== id);
    list_bookDelete.push(id)
    displayBook(listBooks);
    console.log(list_bookDelete);
}

const displayBook = (listBooks) => {
    // Add book to table
    const tableBody = document.querySelector('.container-books__table tbody');

    if (!tableBody) return;
    tableBody.innerHTML = '';

    if (listBooks.length === 0) {
        tableBody.innerHTML = `
            <tr>
                <th colspan="9">Không có sách nào</th>
            </tr>
        `;
        return;
    }

    let stt = 1;
    listBooks.forEach(book => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <th class="align-middle">${stt}</th>
            <td class="align-middle">${book.name}</td>
            <td class="align-middle">${book.author}</td>
            <td class="align-middle">${book.price}</td>
            <td class="align-middle">${book.quantity}</td>
            <td class="align-middle">${book.category.name}</td>
            <td class="align-middle d-table-cell">
                <button type="button" class="btn btn-outline-primary" onclick="handleUpdateBook('${book.id}')" style="margin-right: 8px" title="Sửa">
                    <i class="bi bi-gear"></i>
                </button>
                <button type="button" class="btn btn-outline-danger" onclick="handleDeleteBook('${book.id}')" style="margin-right: 8px" title="Sửa">
                    <i class="bi bi-trash3"></i>
                </button>
            </td>
        `;
        tableBody.appendChild(tr);
        stt++;
    });
    console.log(listBooks);
}

const chooseBook = (element) => {
    const id_book = element.value;
    if (id_book !== '0') {
        console.log(id_book);
        fetch(`/getBookById?id=${element.value}/`)
            .then(response => response.json())
            .then(data => {
                if (data) {
                    bookName.value = data.name;
                    bookAthor.value = data.author;
                    bookPrice.value = data.price;
                    bookCategory.value = data.id_category;
                    bookName.disabled = true;
                    bookAthor.disabled = true;
                    bookCategory.disabled = true;
                }
            })
    } else {
        // Reset value input
        bookName.value = '';
        bookAthor.value = '';
        bookPrice.value = '';
        bookQuantity.value = '';
        bookCategory.selectedIndex = 0;
        bookName.disabled = false;
        bookAthor.disabled = false;
        bookCategory.disabled = false;
    }
}

// Handle get data form phieu nhap
const getDataFormPN = () => {
    if (listBooks.length === 0) {
        alert('Vui lòng nhập sách');
        return;
    }

    // Get value input
    const dvcc = document.querySelector('.dvcungcap').value.trim();
    const ngaynhap = document.querySelector('.ngaynhap').value.trim();
    const lydo = document.querySelector('.lydo').value.trim();

    const data = {
        dvcc,
        ngaynhap,
        lydo,
        books: listBooks
    };

    return data;
}

// Handle submit form lap phieu nhap
const submitAddPhieunhap = (e) => {
    e.preventDefault();
    // Get data form
    const data = getDataFormPN();

    // Submit form
    fetch('/nhapsachPost/', {
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
            if (data.status === true) {
                toastr.success(data.message)
                setTimeout(() => {
                    window.location.href = '/quan-ly-kho-sach/nhap-sach/';
                }, 2000)
            } else {
                toastr.error(data.message)
            }
        })
}

// Handle submit form cap nhat phieu nhap
const submitUpdatePhieunhap = (e) => {
    e.preventDefault();

    // Get data form
    const data = getDataFormPN();

    const id_phieunhap = document.querySelector('.phieunhap-id').value.trim();

    if (!id_phieunhap) {
        alert('Không tìm thấy phiếu nhập sách');
        return;
    }

    data.id_phieunhap = id_phieunhap;
    data.book_deletes = list_bookDelete;
    
    // Submit form
    fetch('/updatePhieunhapPost/', {
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
            if (data.status === true) {
                toastr.success(data.message)
                setTimeout(() => {
                    window.location.href = '/quan-ly-kho-sach/nhap-sach/';
                }, 2000)
            } else {
                toastr.error(data.message)
            }
        })

}

// Handle delete phieu nhap
const deletePhieunhap = (id) => {
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.remove('d-none');
        modal.classList.remove('d-none');
        modal.querySelector('.btn-delete').setAttribute('href', `/quan-ly-kho-sach/nhap-sach/delete/${id}`);
    }
}

const cancelDelete = () => {
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.add('d-none');
        modal.classList.add('d-none');
    }
}

// Search phieu nhap by date
const searchPhieumuonByDate = () => {
    const dateFrom = document.querySelector('#search-date-from').value.trim();
    const dateTo = document.querySelector('#search-date-to').value.trim();

    if (!dateFrom || !dateTo) {
        alert('Vui lòng chọn ngày bắt đầu và ngày kết thúc');
        return;
    }

    console.log(dateFrom, dateTo);
    window.location.href = `/quan-ly-kho-sach/nhap-sach/search/${dateFrom}/${dateTo}`;
}

displayBook(listBooks);

//handle xoá sách
const deleteBook = (id_sach) => {
    //open modal
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.remove('d-none');
        modal.classList.remove('d-none');
        modal.querySelector('.btn-delete').setAttribute('href', `/quan-ly-sach/delete/${id_sach}`);
    }
}

//handle cancel xoá sách
const cancelDeleteBook = () =>{
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.add('d-none');
        modal.classList.add('d-none');
    }
}

//handle tim kiem sach
const searchBook = () => {
    const searchInput = document.querySelector('.search-book');
    const searchValue = searchInput.value.trim();
    if (searchValue){
        window.location.href=`/quan-ly-sach/search/${searchValue}`;
    }
}

//handel cancel tim kiem sach
const searchBookEnter = (event) => {
    if (event.key === 'Enter') {
        searchBook();
    }
}

