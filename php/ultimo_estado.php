<?php

include 'conectar_bd.php';

// Verificar si se ha recibido el parámetro LampID en la solicitud GET
if (isset($_GET['lampID'])) {
    $lampID = $conn->real_escape_string($_GET['lampID']);

    // Obtener el último estado de la lámpara para el LampID proporcionado
    $sqlGetEstado = "SELECT Nreg, LampOnOff FROM t_iotlampv0 WHERE LampID = ? ORDER BY fecha_creacion DESC LIMIT 1";
    $stmtGet = $conn->prepare($sqlGetEstado);
    $stmtGet->bind_param("s", $lampID);
    $stmtGet->execute();
    $resultadoEstado = $stmtGet->get_result();

    if ($fila = $resultadoEstado->fetch_assoc()) {
        $nreg = $fila['Nreg'];
        $estadoActual = $fila['LampOnOff'];
        $nuevoEstado = ($estadoActual == 1) ? 2 : 1;

        // Actualizar el estado de la lámpara y la fecha de creación en el último registro
        $sqlUpdate = "UPDATE t_iotlampv0 SET LampOnOff = ?, fecha_creacion = CURRENT_TIMESTAMP WHERE Nreg = ?";
        $stmtUpdate = $conn->prepare($sqlUpdate);
        $stmtUpdate->bind_param("ii", $nuevoEstado, $nreg);

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
