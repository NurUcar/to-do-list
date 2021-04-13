//open-close collapse
document.querySelectorAll('.to_do_item').forEach(button => {
    button.addEventListener('click', () => {
        const collapseContent = button.nextElementSibling;
        button.classList.toggle('to_do_item--active');
        if (button.classList.contains('to_do_item--active')) {
            collapseContent.style.maxHeight = collapseContent.scroollHeight + 'px';
        } else {

            collapseContent.style.maxHeight = 0;
        }
    });
});