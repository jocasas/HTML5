
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
/* ---------------------------------------------------------- */


$(document).ready(function () {

if (window.location.pathname !== '/index.html') {
    $(".card:first").hide()
    $.ajax({
      url: "/JSON/script.json",
      success: function (result) {
        $.each(result, function (index, item) {
          var cards = $(".card:first").clone() //clona el primer div
          var categoriaCarta = item.categoriaCarta;
          var numCarta = item.numCarta;
          var img = item.img;
          var nombreProd = item.nombreProd;
          var bodyId = item.body;
          var unidad = item.unidades;
          var descripcion = item.desc;
          var price = item.price;
          if (categoriaCarta == 1 && window.location.pathname == '/medicamentos.html') {
            //agrega los datos dentro del div o carta
            /*               $(cards).find(".card-header").html("user id: " + categoriaCarta + " - " + "id: " + numCarta).hide(); */
            $(cards).find(".card-title").html(nombreProd);
            $(cards).find(".card-img-top").attr("src", img);
            $(cards).find(".card-text").html(bodyId);
            $(cards).find(".card-text2").html(unidad);
            $(cards).find(".card-text3").html(descripcion);
            $(cards).find(".card-price").html("$"+ price + " c/u");
            $(cards).show() //muestra las cartas
            $(cards).appendTo($("#container-productos"))

          } else if (categoriaCarta == 2 && window.location.pathname == '/mascotas.html') {
            $(cards).find(".card-title").html(nombreProd);
            $(cards).find(".card-img-top").attr("src", img);
            $(cards).find(".card-text").html(bodyId);
            $(cards).find(".card-text2").html(unidad);
            $(cards).find(".card-text3").html(descripcion);
            $(cards).find(".card-price").html("$" + price + " c/u");
            $(cards).show() //muestra las cartas
            $(cards).appendTo($("#container-mascotas"))
          } else if (categoriaCarta == 3 && window.location.pathname == '/sexualidad.html') {
            $(cards).find(".card-title").html(nombreProd);
            $(cards).find(".card-img-top").attr("src", img);
            $(cards).find(".card-text").html(bodyId);
            $(cards).find(".card-text2").html(unidad);
            $(cards).find(".card-text3").html(descripcion);
            $(cards).find(".card-price").html("$" + price + " c/u");
            $(cards).show() //muestra las cartas
            $(cards).appendTo($("#container-sexualidad"))
          } else if (categoriaCarta == 4 && window.location.pathname == '/belleza.html') {
            $(cards).find(".card-title").html(nombreProd);
            $(cards).find(".card-img-top").attr("src", img);
            $(cards).find(".card-text").html(bodyId);
            $(cards).find(".card-text2").html(unidad);
            $(cards).find(".card-text3").html(descripcion);
            $(cards).find(".card-price").html("$" + price + " c/u");
            $(cards).show() //muestra las cartas
            $(cards).appendTo($("#container-belleza"))
          } 
          

        });
      }
    });
  }
  /* Validaciones Login */

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
  
});