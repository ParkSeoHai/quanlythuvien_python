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

// Handle modal delete user
const deleteUser = (id) => {
    // Open modal
    const modalBg = document.querySelector('.modal-bg');
    const modal = document.querySelector('.modal-delete');
    if (modalBg && modal) {
        modalBg.classList.remove('d-none');
        modal.classList.remove('d-none');
        modal.querySelector('.btn-delete').setAttribute('href', `delete/${id}`);
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
        window.location.href = `/quan-ly-nguoi-dung/search/${searchValue}`;
    }
}

// Handle search user enter key
const searchUserEnter = (event) => {
    if (event.key === 'Enter') {
        searchUser();
    }
}