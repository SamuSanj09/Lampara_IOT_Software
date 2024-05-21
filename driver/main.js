import { verificarConexion } from "./verificarConexion.js";
import { cargarDatos } from "./cargarDatos.js";

document.addEventListener("DOMContentLoaded", function () {
  // Verificar la conexión a la base de datos al cargar la página
  verificarConexion();

  // Cargar los datos y configurar la actualización automática
  document
    .getElementById("cargarDatosBtn")
    .addEventListener("click", function (event) {
      event.preventDefault();
      cargarDatos();
    });

  cargarDatos();
  setInterval(cargarDatos, 5000);

  // Cambiar el estado de la lámpara
  document
    .getElementById("button_cambiar_estado")
    .addEventListener("click", function () {
      const lampID = document.getElementById("lampIDInput").value;
      const userID = document.getElementById("userIDInput").value;
      fetch(`../php/ultimo_estado.php?LampID=${lampID}&UserID=${userID}`)
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            console.log(
              `El nuevo estado de la lámpara ${data.LampID} es: ${data.newState} cambiado por el usuario ${data.UserID}`
            );
          } else {
            console.error(
              `Error al cambiar el estado de la lámpara: ${data.error}`
            );
          }
        })
        .catch((error) =>
          console.error("Error al cambiar el estado de la lámpara:", error)
        );
    });
});
