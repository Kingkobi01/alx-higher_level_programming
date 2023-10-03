$(document).ready(function () {
  $("div#toggle_header").click(function () {
    // $("header").toggleClass(function () {
    //   return $(this).hasClass("red") ? "green" : "red";
    // });
    if ($("header").hasClass("green")) {
      $("header").removeClass("green").addClass("red");
    } else {
      $("header").removeClass("red").addClass("green");
    }
  });
});
