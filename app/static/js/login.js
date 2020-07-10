$(document).ready(function(){
  $("#loginForm").submit(function(e) {
    e.preventDefault();
    $.get({url: "http://localhost:5000/about", success: function(result){
  }});
});
 
});