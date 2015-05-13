function getLastTempResult() {
  $.getJSON('/last/', function( data ) {
    if (typeof data != 'undefined') {
        ar=data.toString().split(".");
        $("#currenttemp").html(  ar[0]  );
        $("#currenttemp_decimal").html(  ar[1]  );
    }
  });
}


function getDayResult(url) {
  $.getJSON(url, function( data ) {
    if (typeof data != 'undefined') {
      return JSON.parse(data);
    }
  });
}



// ----------- charts  ----------- 
google.load('visualization', '1', {packages: ['corechart', 'line']});
google.setOnLoadCallback(drawCurveTypes);

function loadJSON(url) {
    var request = new XMLHttpRequest();

  request.open('GET', url, false);
  request.send();


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
    getLastTempResult();
    ChartCounterDelay++;

    if ( ChartCounterDelay == 100  ) {
       ChartCounterDelay=0;
       drawCurveTypes();
    }

}, 3 * 1000); // 60 * 1000 milsec

$( window ).load(function() {
  getLastTempResult();
});