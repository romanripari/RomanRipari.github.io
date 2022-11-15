let mybutton = document.getElementById("myBtn");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

$(document).mouseup(function(e) {
  if (e.which != 1) return false;

  $('.card--front').toggleClass('card--front--flip');
  $('.card--back').toggleClass('card--back--flip');
});


$('a').mouseup(function(e) {
  e.stopPropagation();
});

