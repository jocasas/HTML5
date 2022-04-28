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
                        $(cards).find(".card-price").html("$" + price + " c/u");
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
});