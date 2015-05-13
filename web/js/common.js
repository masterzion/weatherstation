// ----------- temperatures  ----------- 
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





// ----------- charts  ----------- 
window.setInterval(function(){
    drawCurveTypes()
}, 1000 * 60 * 5 );

google.load('visualization', '1', {packages: ['corechart', 'line']});
google.setOnLoadCallback(drawCurveTypes);

function loadJSON(url) {
    var request = new XMLHttpRequest();

  // load it
  // the last "false" parameter ensures that our code will wait before the
  // data is loaded
  request.open('GET', url, false);
  request.send();

  // parse adn return the output
  return JSON.parse(request.responseText);
};


function drawCurveTypes() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Hour');
  data.addColumn('number', 'Temp1');
//      data.addColumn('number', 'Temp2');

  data.addRows(loadJSON('/day/'));

  var options = {
    backgroundColor: { fill:'transparent' },
    curveType: 'function',
    hAxis: {
      title: 'Hour'
    },
    vAxis: {
      title: 'Temperature'
    },
    series: {
      1: {curveType: 'function'}
    }
  };

  var chart = new google.visualization.LineChart(document.getElementById('chartdiv'));
  chart.draw(data, options);
}

// ----------- auto refresh  ----------- 
ChartCounterDelay=0;
setInterval(function() {
    val = getresult();
    settempvalue (  val );
    ChartCounterDelay++;

    if ( ChartCounterDelay == 100  ) {
       ChartCounterDelay=0;
       drawCurveTypes();
    }

}, 3 * 1000); // 60 * 1000 milsec
