$(document).ready(function () {
  const language = $("input#language_code").val();

  const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${language}`;

  $("#btn_translate").click(function () {
    $.getJSON(url, function (data, _status) {
      $("div#hello").text(data.hello);
    });
  });
});
