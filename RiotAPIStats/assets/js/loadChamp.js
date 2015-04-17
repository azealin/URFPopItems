/**
 * Created by azeal_000 on 4/12/2015.
 */
$(function(){
   var champ = getUrlVars()["champ"]
   var i;
    for (i = 1; i<8; i++){
        if(i ==1 ){
             $(".row").append("<h2 class=\'league\'> Unranked: " + "</div>");
        }
        else if(i == 2){
            $(".row").append("<h2 class=\'league\'> Bronze: " + "</div>");
        }
        else if(i == 3){
            $(".row").append("<h2 class=\'league\'> Silver: " + "</div>");
        }
        else if(i == 4){
            $(".row").append("<h2 class=\'league\'> Gold: " + "</div>");
        }
        else if(i == 5){
            $(".row").append("<h2 class=\'league\'> Platinum: " + "</div>");
        }
        else if(i == 6){
            $(".row").append("<h2 class=\'league\'> Diamond: " + "</div>");
        }
        else if(i == 7){
            $(".row").append("<h2 class=\'league\'> Master/Challenger: " + "</div>");
        }

        $(".row").append(" <div class=\'col-lg-12 col-sm-6 col-xs-8\'> " +
        "<img src=\'../assets/img/"+champ + "_" + i + ".jpg\' class=\'thumbnail img-responsive champ'> </div>");
    }
    $(".lead").html(champ);
});

function getUrlVars() {
      var vars = {};
      var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
      });
      return vars;
}