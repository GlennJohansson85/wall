function formatFileSize(bytes) {
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (bytes === 0) return '0 Byte';
    const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
    return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
}

document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];  // Get the selected file
    const fileSizeDisplay = document.getElementById('fileSize');

    if (file) {
        const fileSize = file.size;  // File size in bytes
        const formattedSize = formatFileSize(fileSize);  // Format it

        // Show the file size to the user
        fileSizeDisplay.textContent = `File size: ${formattedSize}`;

        // Remove any previously applied classes
        fileSizeDisplay.classList.remove('valid-size', 'invalid-size');

        // Check if the file size exceeds the limit (13 MB)
        const maxSize = 13 * 1024 * 1024;  // 13 MB
        if (fileSize > maxSize) {
            fileSizeDisplay.textContent += ' (File exceeds 13 MB limit)';
            fileSizeDisplay.classList.add('invalid-size');  // Apply red color if exceeds limit
        } else {
            fileSizeDisplay.classList.add('valid-size');  // Apply green color if within limit
        }
    }
});
