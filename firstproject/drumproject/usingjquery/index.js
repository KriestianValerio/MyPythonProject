// alert("Hi");

// // $("h1").css("color", "red")
// // $("h1").css("font-size") bisa di console log

// $("h1").addClass("big-title");
// // $("h1").removeClass("big-title");

// // $("h1").hasClass("big-title"); hasilnya boolean

// $("h1").text("big-title");
// $("button").text("baba");
// $("button").html("<em>Dadan</em>");
// $("button").attr("src");
// $("button").attr("src", "link");
// $("a").attr("href","https://www.yahoo.com"); 

// $("h1").click( function() {
//     $("h1").css("color","purple");


// });

// for (var i=0; i<5 ; i++) {
//     document.querySelectorAll("button") [i].addEventListener("click", function() {
//         document.querySelector("h1").style.color = "purple";
//     });
// }

// $("button").click(function() {
//     $("h1").css("color","purple");
// });

// $("input").keydown(function(event){
//     $("h1").text(event.key);
// });

// $("h1").on(" mouseover",function(){
//     $("h1").css("color","purple");   
// });

// $("h1").before("<button>New</button>")
// .append
// .prepend
// .remove
// $("h1").after("<button>New</button>")

// $("button").click(function() {
//    $("h1").hide();
//    // buat show:
//    $("h1").show();
   // buat toggle:
//    $("h1").toggle();
//    $("h1").fadeOut();
//    .fadeIn;
//    .fadeToggle

    // .slideUp or .slideDown or slideToggle
//    $("h1").fadeToggle();
//     });

//// buat animasi

//  $("button").on("click", function () {
//     $("h1").animate({margin : "50%" ,  opacity: 0.5 });
//  });

 $("button").on("click", function () {
   $("h1").slideUp().slideDown().animate({margin : "50%" ,  opacity: 0.5 });
});








