function load_data(query)
  {
   $.ajax({
    url:"/ajaxlivesearch",
    method:"POST",
    data:{query:query},
    success:function(data)
    {
      $('#result').html(data);
      $("#result").append(data.htmlresponse);
    }
   });
  } 

function myFunction() {
  let search = document.getElementById("search_text").value;
//  alert(search);
  if(search != ''){
    load_data(search);
   }else{
    load_data("null");
}
}

window.onload = function() {
  document.getElementById('googleIcon').addEventListener('click', function (e) {
    document.getElementById('searchBox').classList.toggle('active');
  });
};