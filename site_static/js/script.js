$(function () {
    var selectBtn = $("<div class='select-btn'></div>");
    selectBtn.appendTo(".select");

    $('nav ul li').mouseover(function () {
        var item = $(this).find('ul');
        if (!item.is(':animated')) {
            if (!$(this).hasClass("active")) {
                item.slideDown();
                $(this).addClass("active");
            }
        }
    });
    $('nav ul li').mouseleave(function () {
        var item = $(this).find('ul');
        if (!item.is(':animated')) {
            if ($(this).hasClass("active")) {
                item.slideUp();
                $(this).removeClass("active");
            }

        }
    });
    var reviewWrap = $('<div class="review__popup__wrap"></div>'),
        review__block = $('.review__popup'),
        btnSend = $('.review__btn._send');
    review__block.appendTo('body');
    reviewWrap.appendTo('body');

    $(".review__btn").click(function () {
        review__block.fadeIn();
        reviewWrap.fadeIn();
        return false;
    });

    $(".review__close, .review__popup__wrap, .review__btn._send").click(function () {
        review__block.fadeOut();
        reviewWrap.fadeOut();
    });

});