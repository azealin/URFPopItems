/**
 * Created by azeal_000 on 4/12/2015.
 */
$(function(){
   var champ = getUrlVars()["champ"]
   var i;
    for (i = 0; i<7; i++){
        $(".row").append(" <div class=\\'col-lg-2 col-sm-3 col-xs-4\\'> " +
        "<img src=\\'../assets/img/Aatrox_" + i + ".jpg\\' class=\\'thumbnail img-responsive champ'> </div>");
    }
});

function getUrlVars() {
      var vars = {};
      var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
      });
      return vars;
}