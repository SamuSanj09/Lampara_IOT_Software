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
});
