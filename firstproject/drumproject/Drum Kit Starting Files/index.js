

for (var i=0; i<document.querySelectorAll(".drum").length ; i++ ){

    document.querySelectorAll(".drum")[i].addEventListener("click",handleClick);

       

    // ini kasus kalo di klik
};

function handleClick() {
    // alert("I got clicked");
   

    var buttonInnerHTML = this.innerHTML;

    makeSound(buttonInnerHTML);

    buttonAnimation(buttonInnerHTML);
    

// ini kasus kalo keydown
}

document.addEventListener("keydown", function(event){

    makeSound(event.key);

    buttonAnimation(buttonInnerHTML);

});

function makeSound(key) {

        switch (key) {
            case "w":
                var audio = new Audio("sounds/tom-1.mp3");
                audio.play();
                break;
            
            case "a":
                var audio = new Audio("sounds/tom-2.mp3");
                audio.play();
                break;

            case "s":
                var audio = new Audio("sounds/tom-3.mp3");
                audio.play();
                break;
            
            case "d":
                var audio = new Audio("sounds/tom-4.mp3");
                audio.play();
                break;

            case "j":
                var audio = new Audio("sounds/snare.mp3");
                audio.play();
                break;

            case "k":
                var audio = new Audio("sounds/crash.mp3");
                audio.play();
                break;

            case "l":
                var audio = new Audio("sounds/kick-bass.mp3");
                audio.play();
                break;
        
            default:
                console.log(buttonInnerHTML);
                break;
        }

    }

function buttonAnimation(currentKey) {
    var activeButton = document.querySelector("." + currentKey); 
    activeButton.classList.add("pressed");

    setTimeout(function() {
        activeButton.classList.remove("pressed");
    },100);
    }






// document.querySelector("button").addEventListener("click", function () {
//     alert("I got clicked");
// }
// );   ini namanya anonymous function, ga dicall tapi langsung di masukin 

