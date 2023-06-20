function toggleSidebar() {
  var sidebar = document.querySelector('.sidebar');
  sidebar.classList.toggle('active');
}

function toggleMenu(element) {
  var subtitle = element.classList.toggle('open');
  // var menu = document.getElementById('menu');

  // menu.style.display = (menu.style.display === 'block') ? 'none' : 'block';
}
