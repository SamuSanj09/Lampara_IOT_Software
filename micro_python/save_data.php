<?php
// Configuración de la base de datos
$servername = "localhost";
$username = "root";
$password = ""; // Asegúrate de usar una contraseña en un entorno de producción
$database = "db_iotlampv0";

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
    $lamp_id = $conn->real_escape_string($data['LampID']);
    $temp_value = $conn->real_escape_string($data['temp_value']);
    $temp_int = $conn->real_escape_string($data['temp_int']);
    $sep_point = $conn->real_escape_string($data['sep_point']);
    $lamp_on_off = $conn->real_escape_string($data['LampOnOff']);

    // SQL para insertar datos
    $sql = "INSERT INTO t_iotlampv0 (LampID, temp_value, temp_int, sep_point, LampOnOff) VALUES ('$lamp_id', '$temp_value', '$temp_int', '$sep_point', '$lamp_on_off')";

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
