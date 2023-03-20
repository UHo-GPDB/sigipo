function showAddPopup(href, title) {
  var win = window.open(
    href,
    title,
    "height=500,width=800,resizable=yes,scrollbars=yes",
  );
  win.focus();
  return false;
}
function closePopup(win) {
  win.close();
}
window.showAddPopup = showAddPopup;
window.closePopup = closePopup;
