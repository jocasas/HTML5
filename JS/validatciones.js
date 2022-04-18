
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