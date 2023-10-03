$(document).ready(function () {
  $("div#add_item").click(function () {
    var item = document.createElement("li");
    item.textContent = "Item";
    $("ul.my_list").append(item);
  });
});
