$(document).ready(function(){
    $.ajax({ url: "/containers",
        success: function(data){
            $("#containers").text(JSON.stringify(data, null, 2));
        }
    });

    $.ajax({ url: "/info",
        success: function(data){
            $("#info").text(JSON.stringify(data, null, 2));
        }
    });

    $.ajax({ url: "/services",
        success: function(data){
            $("#services").text(JSON.stringify(data, null, 2));
        }
    });
});