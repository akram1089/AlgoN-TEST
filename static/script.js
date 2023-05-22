
var spinner = function () {
    setTimeout(function () {
        if ($('#spinner').length > 0) {
            $('#spinner').removeClass('show');
        }
    }, 1);
};
spinner();

$(window).scroll(function () {

    if ($(window).width() < 992) {
        if ($(this).scrollTop() > 45) {
            $('.fixed-top').addClass('bg-light shadow');
            $('.nav-item, .nav-item a').addClass('text-light');
         
        } else {
            $('.fixed-top').removeClass('bg-light shadow');
            $('.nav-item,.nav-item a').removeClass('text-light');
        }
    } else {
        if ($(this).scrollTop() > 45) {
            $('.nav-item,.nav-item a').addClass('text-dark');
            $('.fixed-top').addClass('bg-light shadow').css('top', 0);
        } else {
            $('.fixed-top').removeClass('bg-light shadow').css('top', 0);
              $('.nav-item,.nav-item a').removeClass('text-dark');
        }
    }
});

$(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
        $('.back-to-top').fadeIn('slow');
    } else {
        $('.back-to-top').fadeOut('slow');
    }
});
// $('.back-to-top').click(function () {
//     $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
//     return false;
// });



      $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    $('.counter').counterUp({
        delay: 10,
        time: 2000
      });
      $('.counter').addClass('animated fadeInDownBig');
      $('h3').addClass('animated fadeIn');





  