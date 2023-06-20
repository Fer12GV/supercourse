
  // Obtener el elemento de la ventana modal
  var modal = document.getElementById("notificationModal");

  // Obtener el elemento <span> que cierra la ventana modal
  var closeBtn = document.getElementsByClassName("close")[0];


  // Cerrar la ventana modal cuando se hace clic en el botón de cierre
  closeBtn.onclick = function() {
    modal.style.display = "none";
  };
