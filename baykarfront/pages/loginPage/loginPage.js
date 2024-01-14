$(document).ready(function(){
    $(".leftMenu").load("/components/leftMenu/leftMenu.html");
});

function showPassword() {
    var x = document.getElementById("password");
    var label = document.getElementById("passLabel");
    if (x.type === "password") {
      x.type = "text";
      label.innerHTML = "Şifreyi Gizle";
    } else {
      x.type = "password";
      label.innerHTML = "Şifreyi Göster";
    }
  }
