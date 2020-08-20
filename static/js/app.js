
$(document).ready(function () {
    alert("in javascript")
   
    
    function getData() {
        /* data route */
      var url = "/api/v1.0/wosdocuments";
      d3.json(url).then(function(response) {
    
        console.log(response);
        var data = [response];
    
        
      });
    }
    
    getData();
    



    
  
});
