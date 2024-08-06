$(document).ready(function(){
    $('.card').click(function(){
        var url = $(this).data('url');
        if(url){
            window.location.href = url;
        }
    });
});