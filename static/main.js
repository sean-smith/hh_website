$( document ).ready(function() {
  $.get("/tiles", function(data){
    console.log("get_request_worked");
    var data = data.all_users;
    for(var i=0; i<data.length; i++){
      var first = data[i].first;
      var last = data[i].last;
      var url = data[i].url;
      var html = "<li class=\"list-group-item\"><a href=\""+url+"\">"+first+" "+last+"</a></li>";
      console.log(html);
      $("#listofhh").append(html);
    }
  });



});
