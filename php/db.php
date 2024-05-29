<?php
// Configuración de la base de datos
$servername = "localhost";
$username = "root";
$password = ""; // Asegúrate de usar una contraseña en un entorno de producción
$database = "prueba_instrumentos";

// Función para crear la conexión a la base de datos
function connect_db() {
    global $servername, $username, $password, $database;
    $conn = new mysqli($servername, $username, $password, $database);

    // Verificar conexión
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}
?>
