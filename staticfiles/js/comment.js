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
    const postElement = document.querySelector(`.concrete[data-post-id="${postId}"]`);

    if (postElement) {
        console.log(`Found post element:`, postElement);  // Debugging line
        postElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
        console.log(`Post with ID ${postId} not found!`);  // Debugging line
    }
}