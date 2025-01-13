/*
Handles the Enter press in comment input field.

Prevents the default action (adding a newline in a textarea or submitting the form)
and instead submits the form programmatically.
 */
function handleKeyPress(event, postId) {
    if (event.key === 'Enter') {
        event.preventDefault();
        const form = document.getElementById('comment-form-' + postId);
        form.submit();
    }
}