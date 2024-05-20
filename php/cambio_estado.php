<?php
$servername = "localhost";
$username = "root";
$password = ""; // Asegúrate de usar una contraseña en un entorno de producción
$database = "lamp";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $database);

// Verificar conexión
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Verificar si se ha recibido el parámetro LampID en la solicitud GET
if (isset($_GET['LampID'])) {
    $lampID = $conn->real_escape_string($_GET['LampID']);

    // Obtener el último estado de la lámpara para el LampID proporcionado
    $sqlGetEstado = "SELECT LampOnOff FROM t_iotlampv0 WHERE LampID = ? ORDER BY fecha_creacion DESC LIMIT 1";
    $stmtGet = $conn->prepare($sqlGetEstado);
    $stmtGet->bind_param("s", $lampID);
    $stmtGet->execute();
    $resultadoEstado = $stmtGet->get_result();

    if ($fila = $resultadoEstado->fetch_assoc()) {
        $estadoActual = $fila['LampOnOff'];
        $nuevoEstado = ($estadoActual == 1) ? 2 : 1;

        // Actualizar el estado de la lámpara en el último registro
        $sqlUpdate = "UPDATE t_iotlampv0 SET LampOnOff = ? WHERE LampID = ? ORDER BY fecha_creacion DESC LIMIT 1";
        $stmtUpdate = $conn->prepare($sqlUpdate);
        $stmtUpdate->bind_param("is", $nuevoEstado, $lampID);

        if ($stmtUpdate->execute()) {
            echo json_encode(["success" => true, "newState" => $nuevoEstado]);
        } else {
            echo json_encode(["success" => false, "error" => $stmtUpdate->error]);
        }
        $stmtUpdate->close();
    } else {
        echo json_encode(["success" => false, "error" => "No se encontró la lámpara con el ID especificado"]);
    }
    $stmtGet->close();
} else {
    echo json_encode(["success" => false, "error" => "LampID no proporcionado en la solicitud"]);
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
