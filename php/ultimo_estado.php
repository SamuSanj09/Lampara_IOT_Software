<?php
include 'conectar_bd.php';

// Verificar si se ha recibido el parámetro LampID en la solicitud GET
if (isset($_GET['LampID']) && isset($_GET['UserID'])) {
    $lampID = $conn->real_escape_string($_GET['LampID']);
    $userID = $conn->real_escape_string($_GET['UserID']);

    // Obtener el último estado de la lámpara para el LampID proporcionado
    $sqlGetEstado = "SELECT LampOnOff FROM t_iotlampv0 WHERE LampID = ? ORDER BY fecha_creacion DESC LIMIT 1";
    $stmtGet = $conn->prepare($sqlGetEstado);
    $stmtGet->bind_param("s", $lampID);
    $stmtGet->execute();
    $resultadoEstado = $stmtGet->get_result();

    if ($fila = $resultadoEstado->fetch_assoc()) {
        $estadoActual = $fila['LampOnOff'];
        $nuevoEstado = ($estadoActual == 1) ? 2 : 1;

        // Verificar si la solicitud es solo para obtener el estado
        if (isset($_GET['obtener_estado']) && $_GET['obtener_estado'] == 'true') {
            echo json_encode(["success" => true, "LampID" => $lampID, "UserID" => $userID, "currentState" => $estadoActual]);
        } else {
            // Insertar un nuevo registro con el nuevo estado de la lámpara
            $sqlInsert = "INSERT INTO t_iotlampv0 (LampID, fecha_creacion, temp_value, temp_int, sep_point, LampOnOff, UserID)
                          SELECT LampID, NOW(), temp_value, temp_int, sep_point, ?, UserID
                          FROM t_iotlampv0
                          WHERE LampID = ?
                          ORDER BY fecha_creacion DESC
                          LIMIT 1";
            $stmtInsert = $conn->prepare($sqlInsert);
            $stmtInsert->bind_param("is", $nuevoEstado, $lampID);

            if ($stmtInsert->execute()) {
                echo json_encode(["success" => true, "newState" => $nuevoEstado, "LampID" => $lampID, "UserID" => $userID]);
            } else {
                echo json_encode(["success" => false, "error" => $stmtInsert->error]);
            }
            $stmtInsert->close();
        }
    } else {
        echo json_encode(["success" => false, "error" => "No se encontró la lámpara con el ID especificado"]);
    }
    $stmtGet->close();
} else {
    echo json_encode(["success" => false, "error" => "LampID o UserID no proporcionado en la solicitud"]);
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
