/**
 * Created by azeal_000 on 4/12/2015.
 */
// function to parse champ name on click
$(function(){
    $(".champ").click(function(){
        var champname = $(this).attr('src');
        var c = champname.substring(14);
        c = c.substring(0, c.length-4)
        window.location.href = "../pages/displayinfo.html?champ=" + c;
    });
});