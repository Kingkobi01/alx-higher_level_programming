$(document).ready(function () {
  $.get(
    "https://fourtonfish.com/hellosalut/?lang=fr",
    function (data, _status) {
      $("DIV#hello").text(data.hello);
    }
  );
});
