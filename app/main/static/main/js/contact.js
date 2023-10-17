$(document).ready(function () {
    const contact = $('.contact');

    contact.hover(function () {
        $(this).stop().animate({
            scale: 1.1,
            rotate: '2deg'
        }, 'fast');
    }, function () {
        $(this).stop().animate({
            scale: 1,
            rotate: '0deg'
        }, 'fast');
    });
});
