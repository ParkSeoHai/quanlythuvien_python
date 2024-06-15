// Handle active sidebar
const pathnameCurrent = window.location.pathname.toLowerCase().split('/');

// Add class active vào thẻ link navbar
const navLinks = document.querySelectorAll('.sidebar .sidebar-link');
navLinks.forEach(navLink => {
    // Get value attribute id
    const valueAttId = navLink.getAttribute('page').toLowerCase();
    if (pathnameCurrent.includes(valueAttId)) {
        navLink.classList.toggle('active');
    }
})