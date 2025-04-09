document.addEventListener('DOMContentLoaded', function () {
    // Format file size in a readable way
    function formatFileSize(bytes) {
        const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
        if (bytes === 0) return '0 Byte'; // Special case for 0 bytes
        const i = Math.floor(Math.log(bytes) / Math.log(1024)); // Find the appropriate size unit
        return (bytes / Math.pow(1024, i)).toFixed(2) + ' ' + sizes[i]; // Return formatted size
    }

    // Handling file input change (Profile Picture)
    function validateProfilePictureFileSizeAndResize(event) {
        const inputElement = event.target;
        const file = inputElement.files[0]; // Get the selected file
        const fileSizeDisplay = document.getElementById('fileSizeProfile'); // Display File Size

        if (file) {
            const fileSize = file.size; // Get the file size in bytes
            const formattedSize = formatFileSize(fileSize); // Format the size to a readable string

            // Display file size to user
            fileSizeDisplay.textContent = `File size: ${formattedSize}`;

            // Remove any previously applied classes (valid or invalid size)
            fileSizeDisplay.classList.remove('valid-size', 'invalid-size');

            // Check if size exceeds the limit (13 MB)
            const maxSize = 10 * 1024 * 1024; // 10 MB
            if (fileSize > maxSize) {
                fileSizeDisplay.classList.add('invalid-size'); // Apply red color if exceeds limit
                return false; // Validation error, prevent further actions
            } else {
                fileSizeDisplay.classList.add('valid-size'); // Within limit
                return true; // Success
            }
        }
    }

    // Event listener for profile picture input changes
    document.getElementById('id_profile_picture').addEventListener('change', function(event) {
        validateProfilePictureFileSizeAndResize(event); // Validate when the profile picture input changes
    });
});
