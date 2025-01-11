document.addEventListener("DOMContentLoaded", function() {

    // Select all alert messages
    var alertMessages = document.querySelectorAll('.alert');

    // Loop through each alert message
    alertMessages.forEach(function(alertMessage) {

        // Add a click event listener to the close button inside the alert message
        var closeButton = alertMessage.querySelector('.close');
        if (closeButton) {
            closeButton.addEventListener('click', function() {
                alertMessage.classList.add('fade-out'); // Class to initiate fade-out

                // After fade-out transition ends, remove the alert from the DOM
                alertMessage.addEventListener('transitionend', function() {
                    alertMessage.remove();
                });
            });
        }

        // Timeout to start the fade-out process after 5 seconds if no manual close
        setTimeout(function() {
            alertMessage.classList.add('fade-out'); // Class to initiate fade-out

            // After fade-out transition ends, remove the alert from the DOM
            alertMessage.addEventListener('transitionend', function() {
                alertMessage.remove();
            });
        }, 5000); // Delay before fade-out starts

    });

});
