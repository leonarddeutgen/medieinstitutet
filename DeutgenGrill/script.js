const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
})


var textElement = document.getElementById("text");
var text = textElement.innerText;
textElement.innerText = "";

var words = text.split(" ");
var index = 0;
var intervalId = setInterval(function() {
  textElement.innerText += words[index] + " ";
  index++;
  if (index === words.length) clearInterval(intervalId);
}, 700);