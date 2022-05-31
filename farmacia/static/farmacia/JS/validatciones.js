
/*---------------BOOOTSTRAP-----------------------------*/
(function () {
  'use strict'
  var forms = document.querySelectorAll('.needs-validation')
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
      }, false)
    })
})()

function deletes (idProducto) {
  swal.fire({
    "title" : "estas seguro?",
    "text" : "esta accion no se puede deshacer",
    "icon" : "question",
    "showCancelButton" : true,
    "cancelButtonText" : "cancelar",
    "confirmButtonText" : "eliminar"
  })
  .then(function(result){
    if(result.isConfirmed) {
          window.location.href = "/delete/" + idProducto
    }
  })
}


/* ---------------------------------------------------------- */
/* Validaciones Login */
$(document).ready(function () {
  $("#btn-login").click(function (event) {
    var usuario = $("#usuario-login").val();
    if (usuario == "") {
      $("#error_usuario_log").fadeIn();
      event.preventDefault();

    } else {
      $("#error_usuario_log").hide();

    }

  });
  
  $("#btn-login").click(function (event) {
    var contrasenna = $("#contrasenna-login").val();
    if (contrasenna == "") {
      $("#error_contrasenna_log").fadeIn();
      event.preventDefault();

    } else {
      $("#error_contrasenna_log").hide();

    }

  });

  $("#bt_reg").click(function (event) {

    //variables
    var pass = $("#clave").val();
    var pass2 = $("#clave2").val();
    var emailreg = /^([a-z A-Z 0-9_\.\-])+\@(([a-z A-Z 0-9\-])+\.)+([a-z A-Z 0-9]{2,4})+$/;
    var email = $('#correo').val();
    var usuario = $('#usuario').val();

    //4.val clave rep
    if (pass2 !== pass || pass2 == "") {
      $("#clave2").focus();
      $("#error4").fadeIn();
      $("#clave2").css({ 'borderColor': '#fa1b1b' })
      event.preventDefault();
    } else {
      $("#error4").hide();
      $("#clave").css({ 'borderColor': '#ffffff' })
    }

    //3.val clave
    if (pass.length = "") {
      $("#clave").focus();
      $("#error3").fadeIn();
      $("#clave").css({ 'borderColor': '#fa1b1b' })
      event.preventDefault();
    } else {
      if (pass.length > 3 && pass.length < 9) {
        $("#error3").hide();
        $("#clave").css({ 'borderColor': '#ffffff' })
      } else {
        $("#clave").focus();
        $("#error3").fadeIn();
        $("#clave").css({ 'borderColor': '#fa1b1b' })

        event.preventDefault();

      }
    }

    //2.val correo  
    if (email == "" || !emailreg.test(email)) {
      $("#correo").focus();
      $("#error2").fadeIn();
      $("#correo").css({ 'borderColor': '#fa1b1b' })
      event.preventDefault();
    } else {
      $("#correo").css({ 'borderColor': '#ffffff' })
      $("#error2").hide();
    }

    //1.val usuario
    if (usuario.length > 3 && usuario.length < 9) {
      $("#error1").hide();
      $("#usuario").css({ 'borderColor': '#ffffff' })
    } else {
      $("#usuario").focus();
      $("#error1").fadeIn();
      $("#usuario").css({ 'borderColor': '#fa1b1b' })
      event.preventDefault();
    }
  });

  mybutton = document.getElementById("myBtn");

  window.onscroll = function() {scrollFunction()};

  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }

});
