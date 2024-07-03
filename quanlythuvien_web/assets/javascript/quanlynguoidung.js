
// Handle active tab
const pathnameUser = window.location.pathname.toLowerCase().split('/');
const tabUsers = document.querySelectorAll('.tab-header');
tabUsers.forEach(tab => {
    if (pathnameUser.includes(tab.getAttribute('tab'))) {
        tab.classList.add('active');
    }
});

// Handle modal delete user
const deleteUser = (id) => {
    // Open modal
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.remove('d-none');
        modal.classList.remove('d-none');
        modal.querySelector('.btn-delete').setAttribute('href', `/quan-ly-nguoi-dung/nguoi-dung/delete/${id}`);
    }
}

// Handle cancel delete user
const cancelDeleteUser = () => {
    // Close modal
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.add('d-none');
        modal.classList.add('d-none');
    }
}



// Handle search user
const searchUser = () => {
    const searchInput = document.querySelector('.search-user');
    const searchValue = searchInput.value.trim();
    if (searchValue) {
        window.location.href = `/quan-ly-nguoi-dung/nguoi-dung/search/${searchValue}`;
    }
}

// Handle search user enter key
const searchUserEnter = (event) => {
    if (event.key === 'Enter') {
        searchUser();
    }
}

// Handle modal delete user
const deleteDocgia = (id) => {
    // Open modal
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.remove('d-none');
        modal.classList.remove('d-none');
        modal.querySelector('.btn-delete').setAttribute('href', `/quan-ly-nguoi-dung/doc-gia/delete/${id}`);
    }
}

// Handle cancel delete user
const cancelDeleteDocgia = () => {
    // Close modal
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.add('d-none');
        modal.classList.add('d-none');
    }
}

// Handle search user
const searchDocgia = () => {
    const searchInput = document.querySelector('.search-user');
    const searchValue = searchInput.value.trim();
    if (searchValue) {
        window.location.href = `/quan-ly-nguoi-dung/doc-gia/search/${searchValue}`;
    }
}

// Handle search user enter key
const searchDocgiaEnter = (event) => {
    if (event.key === 'Enter') {
        searchDocgia();
    }
}