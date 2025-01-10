function validateFileSizeAndResize() {
    const fileInput = document.getElementById('id_img');
    const file = fileInput.files[0];
    const maxSize = 13 * 1024 * 1024; // 13 MB

    // If file size exceeds the limit, alert but don't stop the form submission
    if (file && file.size > maxSize) {
        alert("File size exceeds the 13 MB limit! But it will be resized server-side.");
    }

    // Allow the form submission to proceed to the backend for resizing
    return true;
}