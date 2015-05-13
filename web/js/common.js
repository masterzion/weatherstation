function getLastTempResult() {
  $.getJSON('/last/', function( data ) {
    if (typeof data != 'undefined') {
        ar=data.toString().split(".");
        $("#currenttemp").html(  ar[0]  );
        $("#currenttemp_decimal").html(  ar[1]  );
    }
  });
}

// ----------- charts  ----------- 
google.load('visualization', '1', {packages: ['corechart', 'line']});
google.setOnLoadCallback(drawCurveTypes);

function drawCurveTypes() {
  $.getJSON('/day/', function( jsondata ) {
    if (typeof jsondata != 'undefined') {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Hour');
        data.addColumn('number', 'Temp1');
      //      data.addColumn('number', 'Temp2');

        data.addRows( jsondata );

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
  });
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