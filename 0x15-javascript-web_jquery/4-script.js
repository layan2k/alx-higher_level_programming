$(document).ready(function () {
  $('#red_header').click(function () {
    $('#red_header').addClass('red');
    if ($('header').hasClass('red')) {
      ($('header').toggleClass('green'));
    }
    if ($('header').hasClass('green')) {
      ($('header').toggleClass('red'));
    }
  });
});
