function validateFileSizeAndResize() {
    const fileInput = document.getElementById('id_img');
    const file = fileInput.files[0];
    const maxSize = 13 * 1024 * 1024; // 13 MB

    // If file size exceeds the limit, alert and clear the input
    if (file.size > maxSize) {
        alert("File size exceeds the 13 MB limit!");
        fileInput.value = '';
        return;
    }

    const reader = new FileReader();

    reader.onload = function (e) {
        const img = new Image();
        img.src = e.target.result;

        img.onload = function () {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');

            const maxWidth = 1200; // Max width for the resized image
            const maxHeight = 1200; // Max height for the resized image
            let width = img.width;
            let height = img.height;

            // Resize image to fit within maxWidth and maxHeight while maintaining aspect ratio
            if (width > height) {
                if (width > maxWidth) {
                    height = Math.round(height * maxWidth / width);
                    width = maxWidth;
                }
            } else {
                if (height > maxHeight) {
                    width = Math.round(width * maxHeight / height);
                    height = maxHeight;
                }
            }

            // Set the canvas dimensions and draw the resized image
            canvas.width = width;
            canvas.height = height;
            ctx.drawImage(img, 0, 0, width, height);

            // Convert canvas to a blob and create a new file object
            canvas.toBlob(function (blob) {
                const resizedFile = new File([blob], file.name, {
                    type: file.type
                });

                // Replace the original file with the resized one in the file input
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(resizedFile);
                fileInput.files = dataTransfer.files;
            }, file.type);
        };
    };

    reader.readAsDataURL(file);
}
