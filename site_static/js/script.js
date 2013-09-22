$(function(){
    var service =  $(".services ul").find('li');
    service.click(function(){
        $(this).toggleClass("_active");
    });
    var selectBtn = $("<div class='select-btn'></div>");
      selectBtn.appendTo(".select");

    $('nav ul li').hover(function(){
         $(this).find('ul').slideToggle();
    });
    var reviewWrap =  $('<div class="review__popup__wrap"></div>'),
        review__block = $('.review__popup'),
        btnSend = $('.review__btn._send');
    review__block.appendTo('body');
    reviewWrap.appendTo('body');

    $(".review__btn").click(function(){
        review__block.fadeIn();
        reviewWrap.fadeIn();
        return false;
    });

    $(".review__close, .review__popup__wrap, .review__btn._send").click(function(){
        review__block.fadeOut();
        reviewWrap.fadeOut();
    });

});