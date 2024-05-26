<?php
// Configuración de la base de datos
$servername = "localhost";
$username = "root";
$password = ""; // Asegúrate de usar una contraseña en un entorno de producción
$database = "prueba_instrumentos";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $database);

// Verificar conexión
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Leer datos JSON desde el cuerpo de la petición
$input = file_get_contents("php://input");
$data = json_decode($input, true);

if (!empty($data)) {
    $id1 = $conn->real_escape_string($data['id1']); // Cambia 'LampID' por 'id1' para que coincida con los datos de MicroPython
    $valor = $conn->real_escape_string($data['valor']); // Cambia 'temp_value' por 'valor' para que coincida con los datos de MicroPython

    // SQL para insertar datos
    $sql = "INSERT INTO instrumento (id1, valor) VALUES ('$id1', '$valor')";

    // Ejecutar consulta
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
} else {
    echo "No data received";
}

// Cerrar conexión
$conn->close();
?>
