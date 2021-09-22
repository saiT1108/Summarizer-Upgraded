window.addEventListener('DOMContentLoaded, (event) => {

  console.log("Everything Ready :)");

  document.getElementById("summarybutton").addEventListener('click', function() {
    var text = document.getElementById('summarybox');
    text.value = 'hi';
    alert("Hello! I am an alert box!!");
  });

}');
