$(document).ready(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    function (data, _status) {
      var character = data.name;
      $("div#character").text(character);
    }
  );
});
