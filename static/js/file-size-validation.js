function validateFileSize() {
    const fileInput = document.getElementById('id_img');
    const file = fileInput.files[0];
    const maxSize = 13 * 1024 * 1024; // 13 MB

    if (file.size > maxSize) {
        alert("File size exceeds the 13 MB limit!");
        fileInput.value = ''; // Clear the file input
    }
}