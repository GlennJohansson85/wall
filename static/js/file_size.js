// Format file size in a readable way
function formatFileSize(bytes) {
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (bytes === 0) return '0 Byte'; // Special case for 0 bytes
    const i = Math.floor(Math.log(bytes) / Math.log(1024)); // Find the appropriate size unit
    return (bytes / Math.pow(1024, i)).toFixed(2) + ' ' + sizes[i]; // Return formatted size
}

// Handling file input change (Post & Edit Profile)
function validateFileSizeAndResize(event) {
    const inputElement = event.target;
    const file = inputElement.files[0]; // Get the selected file
    const fileSizeDisplay = document.getElementById('fileSize'); // Display File Size

    if (file) {
        const fileSize = file.size; // Get the file size in bytes
        const formattedSize = formatFileSize(fileSize); // Format the size to a readable string

        // Display filesize to user
        fileSizeDisplay.textContent = `File size: ${formattedSize}`;

        // Remove any previously applied classes (valid or invalid size)
        fileSizeDisplay.classList.remove('valid-size', 'invalid-size');

        // Check if size exceeds the limit (13 MB)
        const maxSize = 13 * 1024 * 1024; // 13 MB
        if (fileSize > maxSize) {
            fileSizeDisplay.classList.add('invalid-size'); // Apply red color if exceeds limit
            event.preventDefault(); // Prevent form submission or action
            return false; // = Validation Error
        } else {
            fileSizeDisplay.classList.add('valid-size'); // Within Limit
            return true; // True when success
        }
    }
}

// Event lister
document.getElementById('fileInput').addEventListener('change', function(event) {
    validateFileSizeAndResize(event); // Validate when the post image input changes
});

document.getElementById('id_profile_picture').addEventListener('change', function(event) {
    validateFileSizeAndResize(event); // Validate when the profile picture input changes
});
