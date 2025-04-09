document.addEventListener('DOMContentLoaded', function() {
    // Ensure this script works every time the page is loaded or reloaded
    const urlParams = new URLSearchParams(window.location.search);
    const postId = urlParams.get('post_id');

    if (postId) {
        console.log(`Scrolling to post with ID: ${postId}`);  // Debugging line
        scrollToPost(postId);
    }
});

function scrollToPost(postId) {
    // Find the post with the corresponding data-post-id
    const postElement = document.querySelector(`.concrete[data-post-id="${postId}"]`);

    if (postElement) {
        console.log(`Found post element:`, postElement);  // Debugging line
        postElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
        console.log(`Post with ID ${postId} not found!`);  // Debugging line
    }
}

// Handles the Enter press in comment input field
function handleKeyPress(event, postId) {
    if (event.key === 'Enter') {
        event.preventDefault();

        // Find the form by its ID
        const form = document.getElementById('comment-form-' + postId);

        // Submit the form programmatically
        form.submit();

        // After submitting, scroll to the post and highlight the comment
        setTimeout(function() {
            scrollToPost(postId);

            // Find the most recently added comment and apply the highlight effect
            const commentList = document.querySelectorAll('.postwall-comments-li');
            const lastComment = commentList[commentList.length - 1]; // Get the most recent comment

            if (lastComment) {
                lastComment.classList.add('highlight-comment'); // Add the highlight class
            }
        }, 300); // Wait 300ms to ensure the form submission happens first
    }
}
