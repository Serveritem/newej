(function ($) {
    "use strict";

    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });
})(jQuery);


const scriptURL = 'https://script.google.com/macros/s/AKfycbzn-XZtEB4kqFjmEMJNaKOtYEHdySETZdiiExmgI_sul9qtKe8Nc-ZJ7sZIUWdWSuFj/exec'

const form= document.forms['contact-form']
form.addEventListener('submit', e => {
e.preventDefault()
fetch(scriptURL,{ method: 'POST',body: new Formdata(form)})
.then(response=>alert("Thankyou! your form is submitted Succesfully."))
.ten(() => {window.location.reload();})
.catch(error=> console.error('Error',error.message))
})




