export function verificarConexion() {
  fetch("../php/conectar_bd.php")
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        console.error(data.error);
      } else {
        console.log("Conexión exitosa");
      }
    })
    .catch((error) =>
      console.error("Error al conectar a la base de datos:", error)
    );
}
