
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
  
          form.classList.add('was-validated')
        }, false)
      })
  })()

$(document).ready(function () {
      $("#btn-login").click(function (event) { 
          var usuario = $("#usuario-login").val();
          if (usuario ==  "") {
              $("#error_usuario_log").fadeIn();
              event.preventDefault();

          } else {
              $("#error_usuario_log").hide();

          }
          
      });
});

$(document).ready(function () {
  $("#btn-login").click(function (event) { 
      var contrasenna = $("#contrasenna-login").val();
      if (contrasenna ==  "") {
          $("#error_contrasenna_log").fadeIn();
          event.preventDefault();

      } else {
          $("#error_contrasenna_log").hide();

      }
      
  });
});
//VALIDACIONES REGISTRO
//4.val rep clave
$(bt_reg).click(function(event){
  var pass = $("#clave").val();
  var pass2 = $("#clave2").val();

  if(pass2 !== pass || pass2 == ""){
    
    $("#clave2").focus();
    $("#error4").fadeIn();
    $("#clave2").css({'borderColor':'#fa1b1b'})
    event.preventDefault();
  }else{
    $("#error4").hide();
    $("#clave").css({'borderColor':'#ffffff'})

  }
});

//3.val clave
$(bt_reg).click(function(event){
  var pass = $("#clave").val();
  if(pass.length=""){
    $("#clave").focus();
    $("#error3").fadeIn();
    $("#clave").css({'borderColor':'#fa1b1b'})
    event.preventDefault();
  }else{
    if(pass.length > 3 && pass.length < 9){
      $("#error3").hide();
      $("#clave").css({'borderColor':'#ffffff'})
    }else{
      $("#clave").focus();
      $("#error3").fadeIn();
      $("#clave").css({'borderColor':'#fa1b1b'})
      
      event.preventDefault();

    }
  }
});

//2.val correo
$(bt_reg).click(function(event){
  var emailreg = /^([a-z A-Z 0-9_\.\-])+\@(([a-z A-Z 0-9\-])+\.)+([a-z A-Z 0-9]{2,4})+$/;
  var email = $('#correo').val();

  if(email == "" || !emailreg.test(email)){
    $("#correo").focus();
    $("#error2").fadeIn();
    $("#correo").css({'borderColor':'#fa1b1b'})
    event.preventDefault();
  }else{
    $("#correo").css({'borderColor':'#ffffff'})
    $("#error2").hide();
  }
});  

//1.val usuario
$(bt_reg).click(function(event){
  var usuario = $('#usuario').val();
  if(usuario.length > 3 && usuario.length < 9){
    $("#error1").hide();
    $("#usuario").css({'borderColor':'#ffffff'})
  }else{
    $("#usuario").focus();
    $("#error1").fadeIn();
    $("#usuario").css({'borderColor':'#fa1b1b'})
    event.preventDefault();
  }
});  
//VALIDACIONES REGISTRO
