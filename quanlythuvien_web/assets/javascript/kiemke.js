
let ct_kiemkes = [];
let fileKiemke = null;

// Display table kiemke
const displayTableKiemke = (ct_kiemkes) => {
    const table = document.querySelector('.container-kiemke__table table tbody');
    table.innerHTML = '';
    if (table) {
        ct_kiemkes.forEach(ct => {
            const tr = `
                <th scope="row">${ct.id_sach}</th>
                <td>${ct.name}</td>
                <td>${ct.author}</td>
                <td>${ct.category}</td>
                <td class="text-center">${ct.so_luong_bandau}</td>
                <td class="text-center">${ct.so_luong_kiemke}</td>
                <td class="text-center">${ct.chenh_lech}</td>
            `;
            table.innerHTML += tr;
        });
    }
}

// Get data by file excel from server
const nhapFileExcel = () => {
    const fileElement = document.getElementById('file-kiemke');
    const fileItem = fileElement.files[0];

    if (fileItem) {
        const data = {
            'fileName': fileItem.name
        }
        fileKiemke = fileItem;
        // Request to server
        fetch(`/get_dataKiemkeFile/`, {
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
                    // Display ct kiemke
                    ct_kiemkes = data.data;
                    displayTableKiemke(ct_kiemkes);
                } else {
                    toastr.error(data.message);
                }
            })
    } else {
        toastr.info('Chọn file để thực hiện');
        fileElement.focus();
    }
}

// Upload file to cloudinary
async function uploadFileKiemke(file) {
    const cloudName = 'dvtvl2un6';
    const unsignedUploadPreset = 'sqsfjomd';
    const url = `https://api.cloudinary.com/v1_1/${cloudName}/upload`;

    const fd = new FormData();
    fd.append('folder', 'kiem_ke');
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

// Add phieu kiemke
const submitKiemke = async (event) => {
    event.preventDefault();
    // Get data phieu kiem ke
    const ly_do_kiem_ke = document.querySelector('.lydokiemke');
    const ly_do_value = ly_do_kiem_ke.value.trim();
    if (ly_do_value === "") {
        toastr.info('Nhập lý do kiểm kê');
        ly_do_kiem_ke.focus();
        return;
    }
    // Check data kiem ke
    if (ct_kiemkes.length > 0) {
        // Upload file kiemke
        const responseUpload = await uploadFileKiemke(fileKiemke);
        // Get data
        const data = {
            'ly_do': ly_do_value,
            'file_kiemke': responseUpload.secure_url,
            'ct_kiemkes': ct_kiemkes
        }
        
        // Send request to server
        fetch(`/addPhieuKiemkePost/`, {
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
                        window.location.href = '/quan-ly-kho-sach/kiem-ke';
                    }, 2000);
                } else {
                    toastr.error(data.message);
                }
            })
    } else {
        toastr.info('Thông tin kiểm kê đang trống');
    }
}