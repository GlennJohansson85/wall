function validateFileSizeAndResize() {
    const fileInput = document.getElementById('id_img');
    const file = fileInput.files[0];
    const maxSize = 13 * 1024 * 1024; // 13 MB

    // If file size exceeds the limit, alert and stop the form submission
    if (file && file.size > maxSize) {
        alert("File size exceeds the 13 MB limit!");
        fileInput.value = ''; // Clear the input field
        return false; // Prevent form submission
    }

    // If the file is valid, continue with the form submission
    return true;
}