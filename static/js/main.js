$(document).ready(function(){
    $.ajax({ url: "/containers",
        success: function(data){
            $("#containers").text(data);
        }
    });

    $.ajax({ url: "/info",
        success: function(data){
            $("#info").text(data);
        }
    });

    $.ajax({ url: "/services",
        success: function(data){
            $("#services").text(data);
        }
    });
});