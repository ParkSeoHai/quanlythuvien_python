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

const cancelDelete = () => {
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.add('d-none');
        modal.classList.add('d-none');
    }
}

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

// Click modal background
const modalBg = document.querySelector('.modal-bg');
modalBg.addEventListener('click', () => {
    const modalAddPhieumuon = document.querySelector('.modal-add-phieumuon');
    const modalUpdatePhieumuon = document.querySelector('.modal-update-phieumuon');
    const modalDelete = document.querySelector('.modal-delete');
    const modalConfirmTraSach = document.querySelector('.modal-trasach-phieumuon');

    // Add class d-none
    if (modalAddPhieumuon) modalAddPhieumuon.classList.add('d-none');
    if (modalUpdatePhieumuon) modalUpdatePhieumuon.classList.add('d-none');
    if (modalBg) modalBg.classList.add('d-none');
    if (modalDelete) modalDelete.classList.add('d-none');
    if (modalConfirmTraSach) modalConfirmTraSach.classList.add('d-none');
})