var numberOfdrums = document.querySelectorAll(".drum").length;

for(var i = 0; i<numberOfdrums; i++){

    document.querySelectorAll("button")[i].addEventListener("click", function (){
        alert("I got clicked");
    });
}
