(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    
    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";
    
    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
            function() {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            },
            function() {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);

// Data Picker
document.addEventListener('DOMContentLoaded', function() {
    var selectInputs = document.querySelectorAll("select.form-control");
    selectInputs.forEach(function(selectInput) {
        var firstOption = selectInput.querySelector('option');
        if (firstOption.value === '') {
            firstOption.textContent = "Select";
        }
    });

    // Date picker initialization
    $('.datepicker').datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
        todayHighlight: true
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var livingField = document.getElementById('living');
    var phoneNumberField = document.getElementById('phone_number');
    var emailField = document.getElementById('email');

    if (phoneNumberField && emailField) { // Check if elements exist
        phoneNumberField = phoneNumberField.parentElement;
        emailField = emailField.parentElement;

        function toggleFields() {
            if (livingField.value === 'Yes') {
                phoneNumberField.style.display = '';
                emailField.style.display = '';
            } else {
                phoneNumberField.style.display = 'none';
                emailField.style.display = 'none';
            }
        }

        livingField.addEventListener('change', toggleFields);

        toggleFields();
    } else {
        console.error("Elements with IDs 'phone_number' and 'email' not found.");
    }
});

function logout() {
    var form = document.createElement("form");
    form.method = "POST";
    form.action = "{% url 'account:logout' %}";
    
    var csrf_token = document.createElement("input");
    csrf_token.setAttribute("type", "hidden");
    csrf_token.setAttribute("name", "csrfmiddlewaretoken");
    csrf_token.value = "{{ csrf_token }}";
    
    form.appendChild(csrf_token);
    document.body.appendChild(form);
    
    form.submit();
}

// scholarship
function toggleDetails(index) {
    var details = document.getElementById('details-' + index);
    if (details.style.display === 'none' || details.style.display === '') {
        details.style.display = 'block';
    } else {
        details.style.display = 'none';
    }
}