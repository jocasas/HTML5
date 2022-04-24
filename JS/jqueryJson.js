/* $(document).ready(function(){
    $.get('/HTML5/JSON/script.json',function(data){
        //console.log(data);
        $.each(data.categories,function(i,item){
            $("#categorias").append(
                "<tr><td>" + item.idCategory + "</td> <td>" + item.strCategory + "</td><td><img src='" +
                item.strCategoryThumb + "'></td> <td>" + item.strCategoryDescription + "</td></tr>"
            );
        });

    });
});
 */
/* 
$(function() {
    //hide first div or remove after append using `$(".card:first").remove()`
    $(".card:first").hide()
    $.ajax({
      url: "https://jsonplaceholder.typicode.com/posts",
      success: function(result) {
        $.each(result, function(index, item) {
          var cards = $(".card:first").clone() //clone first divs
          var userId = item.userId;
          var typeId = item.id;
          var titleId = item.title;
          var bodyId = item.body;
          //add values inside divs
          $(cards).find(".card-header").html("user id: " + userId + " - " + "id: " + typeId);
          $(cards).find(".card-title").html(titleId);
          $(cards).find(".card-text").html(bodyId);
          $(cards).show() //show cards
          $(cards).appendTo($(".container")) //append to container
        });
      }
    });
  });

$$(document).ready(function(){

}); */

/* <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous" />

    <div class="row row-cols-md-2 row-cols-md-5 g-2">
        
        <div class="card h-80 text-white bg-dark" style="width: 350px; margin: 10px; display: flex; align-items: center; ">
            <!-- put item.userId & item.id below this -->
            <div class="card-header"></div>
            <div class="card-body">
                <!-- put item.title below this -->
                <h5 class="card-title"></h5>
                <!-- put item.body below this -->
                <p class="card-text"></p>
            </div>
        </div>
    </div> */

/*     <div class="row row-cols-md-1 row-cols-md-1 g-2 wrapper" style="display: flex; justify-content: center;">
        <div class="card h-80 text-white bg-dark" style="width: 350px; margin: 10px; display: flex; align-items: center; ">
            <!-- put item.userId & item.id below this -->
            <div class="card-header"></div>

            <div class="card-body">
            <!-- put item.title below this -->
            <h5 class="card-title"></h5>
            <!-- put item.body below this -->
            <p class="card-text"></p>
            </div>
        </div>
    </div>

    
<section>
<div class="card" style="width: 18rem;">
    <img class="card-img-top" src="img/med_img/ffd91a748ab3afc1f3da1ff471d8f7a5.jpg" alt="Card image cap">
    <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
            card's content.</p>
        <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>
</div>
</section>

 */