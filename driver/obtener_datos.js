document.addEventListener("DOMContentLoaded", function () {
  function obtenerDatos() {
    const lampID = "Lamp02";
    const userID = document.getElementById("userIDInput").value;

    fetch(`obtener_datos.php?lamp_id=${lampID}&user_id=${userID}`)
      .then((response) => response.json())
      .then((data) => {
        // Aquí puedes manejar los datos obtenidos, por ejemplo, actualizando gráficos
        console.log(data);
      })
      .catch((error) => console.error("Error al obtener los datos:", error));
  }

  document
    .getElementById("formulario_lamp_id")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      obtenerDatos();
    });

  document
    .getElementById("button_cambiar_estado")
    .addEventListener("click", function () {
      const lampID = document.getElementById("lampIDInput").value;
      fetch(`cambia_estado.php?lamp_id=${lampID}`)
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            alert(
              "Estado cambiado a: " +
                (data.newState === 1 ? "Apagado" : "Encendido")
            );
            // Recargar los datos
            document
              .getElementById("formulario_lamp_id")
              .dispatchEvent(new Event("submit"));
          } else {
            console.error("Error:", data.error);
          }
        })
        .catch((error) => console.error("Error en la solicitud:", error));
    });

  // Cargar los datos inicialmente
  obtenerDatos();
});
