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
  setInterval(cargarDatos, 10000);

  // Manejar el cambio de estado de la lámpara
  document
    .getElementById("button_cambiar_estado")
    .addEventListener("click", function () {
      const lampID = document.getElementById("lampIDInput").value;
      fetch(`../php/ultimo_estado.php?lampID=${lampID}`)
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            console.log(`Estado de la lámpara cambiado a: ${data.newState}`);
            cargarDatos(); // Volver a cargar los datos para actualizar los gráficos
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
