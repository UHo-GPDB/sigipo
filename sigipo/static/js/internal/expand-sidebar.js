$(document).ready(function () {
  let link = $("main").data("path");
  $(`a[href="${link}"]`).addClass("active-link");
  $(`a[href="${link}"]`).parents("div.collapse").addClass("show");
  $(`a[href="${link}"]`)
    .parents("div.collapse")
    .find("button.btn-toggle")
    .attr("aria-expanded", true)
    .removeClass("collapsed");
});
