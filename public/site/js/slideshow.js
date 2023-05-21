var slideIndex = 0;
slideshow();

function slideshow() {
  var i;
  var slides = document.getElementsByClassName(".slidelist img");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1
  }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(slideshow, 2000); // Change image every 2 seconds
}