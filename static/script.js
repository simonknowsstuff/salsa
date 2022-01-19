  
function open_form() {
  document.getElementById('form_container').style.display = "flex";
  document.getElementById('confirm_title').value = document.getElementById('portfolio_title').value;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function close_form() {
  document.getElementById('form_container').style.display = "none";
}
