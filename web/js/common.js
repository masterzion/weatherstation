
function settempvalue(value){
    value+="";
    if ( value.indexOf('.') == 0 ) {
      value+=".0"
    } 
    ar=value.split(".");
    $("#currenttemp").html(  ar[0]  );
    

    $("#currenttemp_decimal").html(  ar[1]  );
}

function getresult() {
  $.getJSON( "/last/", function( data ) {
     res=data;
  });

  if (typeof res == 'undefined') {
     return '0.0'
  } else {
    return res;
  }  
}

setInterval(function() {
    val = getresult();
    settempvalue (  val );
}, 1 * 1000); // 60 * 1000 milsec
