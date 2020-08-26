
$(document).ready(function () {
    // alert("in javascript")
   
    
    function getwosdocumentcountries() {
        /* data route */
        // https://plotly.com/javascript/pie-charts/
      var url = "/api/v1.0/wosdocumentscountries";
      d3.json(url).then(function(response) {
        Countries_Regions = [];
        Percent = [];
        Records = [];
        var i;
        for (i = 0; i < response.length; i++) {
          Countries_Regions.push(response[i].Countries_Regions)
          Percent.push(response[i].percent)
          Records.push(response[i].records)
        }
          
        // console.log(Countries_Regions)
        // console.log(Percent)
        // console.log(Records)
        // console.log(response)
        // console.log(response[0].Countries_Regions);

        var ultimateColors = [
          ['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)', 'rgb(36, 55, 57)', 'rgb(6, 4, 4)'],
          ['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)', 'rgb(129, 180, 179)', 'rgb(124, 103, 37)'],
          ['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)', 'rgb(175, 49, 35)', 'rgb(36, 73, 147)'],
          ['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)', 'rgb(175, 51, 21)', 'rgb(35, 36, 21)']
        ];
        var data = [{
          values: Records,
          labels: Countries_Regions,
          type: 'pie',
          name: 'Starry Night',
          marker: {
            colors: ultimateColors[0]
          },
          domain: {
            row: 0,
            column: 0
          },
          hoverinfo: 'label+percent+name',
          textinfo: 'none'
        },{
          values: Records,
          labels: Countries_Regions,
          type: 'pie',
          name: 'Sunflowers',
          marker: {
            colors: ultimateColors[1]
          },
          domain: {
            row: 1,
            column: 0
          },
          hoverinfo: 'label+percent+name',
          textinfo: 'none'
        },{
          values: Records,
          labels: Countries_Regions,
          type: 'pie',
          name: 'Irises',
          marker: {
            colors: ultimateColors[2]
          },
          domain: {
            row: 0,
            column: 1
          },
          hoverinfo: 'label+percent+name',
          textinfo: 'none'
        },{
          values: Records,
          labels: Countries_Regions,
          type: 'pie',
          name: 'The Night Cafe',
          marker: {
            colors: ultimateColors[3]
          },
          domain: {
            x: [0.52,1],
            y: [0, 0.48]
          },
          hoverinfo: 'label+percent+name',
          textinfo: 'none'
        }];
        
        var layout = {
          height: 400,
          width: 500,
          grid: {rows: 2, columns: 2}
        };
        
        Plotly.newPlot('pie-chart', data, layout);
    
        
      });
    }
    
    // getwosdocumentcountries();
    



    
  
});
