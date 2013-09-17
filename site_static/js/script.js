$(function(){
    var service =  $(".services ul").find('li');
    service.click(function(){
         service.removeClass('_active');
        $(this).addClass("_active");
    });
    var selectBtn = $("<div class='select-btn'></div>");
      selectBtn.appendTo(".select");
    $(document).bind('click','.select-btn', function(){

     });


    $('.img').click(function(e) {
    $('.img').hide();
    $(document.elementFromPoint(e.clientX, e.clientY)).trigger("click");
    $('.img').show();
});
});