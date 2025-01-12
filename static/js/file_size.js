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

        // Display file size to user
        fileSizeDisplay.textContent = `File size: ${formattedSize}`;

        // Remove any previously applied classes (valid or invalid size)
        fileSizeDisplay.classList.remove('valid-size', 'invalid-size');

        // Check if size exceeds the limit (13 MB)
        const maxSize = 13 * 1024 * 1024; // 13 MB
        if (fileSize > maxSize) {
            fileSizeDisplay.classList.add('invalid-size'); // Apply red color if exceeds limit
            return false; // Validation error, prevent further actions
        } else {
            fileSizeDisplay.classList.add('valid-size'); // Within limit
            return true; // Success
        }
    }
}

// Handle form submission (triggered by submit button)
function handleFormSubmit(event) {
    const fileInput = document.getElementById('fileInput');
    const fileInputProfile = document.getElementById('id_profile_picture');

    // Validate the file size for both inputs
    const isFileValid = validateFileSizeAndResize({ target: fileInput }) && validateFileSizeAndResize({ target: fileInputProfile });

    // If any file size is invalid, prevent form submission
    if (!isFileValid) {
        event.preventDefault(); // Prevent form submission
        alert("File size exceeds the 13 MB limit.");
        return false; // Prevent form submission
    }

    return true; // Proceed with form submission
}

// Event listener for file input changes
document.getElementById('fileInput').addEventListener('change', function(event) {
    validateFileSizeAndResize(event); // Validate when the post image input changes
});

document.getElementById('id_profile_picture').addEventListener('change', function(event) {
    validateFileSizeAndResize(event); // Validate when the profile picture input changes
});

// Event listener for submit button (name="submit")
document.querySelector('button[name="submit"]').addEventListener('click', function(event) {
    handleFormSubmit(event); // Handle form submission
});
