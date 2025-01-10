function validateFileSize() {
    const fileInput = document.getElementById('id_img');
    const file = fileInput.files[0];
    const maxSize = 20 * 1024 * 1024; // 20 MB

    if (file.size > maxSize) {
        alert("File size exceeds the 20 MB limit!");
        fileInput.value = ''; // Clear the file input
    }
}