$(document).ready(function () {
  $("div#add_item").click(function () {
    const li = document.createElement("li");
    $(li).text("Item");
    $("ul.my_list").append(li);
  });
  $("div#remove_item").click(function () {
    $("ul.my_list li:last-child").remove(); //removes last li element
  });
  $("div#clear_list").click(function () {
    $("ul.my_list").text(null);
  });
});
