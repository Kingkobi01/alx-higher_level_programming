$(document).ready(function () {
  $.get(
    "https://swapi-api.alx-tools.com/api/films/?format=json",
    function (data, _status) {
      var movies = data.results;
      var ul = $("ul#list_movies");
      for (let movie of movies) {
        var li = document.createElement("li");
        $(li).text(movie.title);
        ul.append(li);
      }
    }
  );
});
