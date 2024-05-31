<?php
include 'db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Leer datos JSON desde el cuerpo de la petición
    $input = file_get_contents("php://input");
    $data = json_decode($input, true);

    if (!empty($data)) {
        $nombre_instrumento = $data['nombre_instrumento'];
        $valor = $data['valor'];
        $sonido = $data['sonido'];
        $HoraFecha = date('Y-m-d H:i:s');

        $sql = "INSERT INTO instrumento (valor, sonido, HoraFecha, nombre_instrumento) VALUES (?, ?, ?, ?)";
        $stmt = $conn->prepare($sql);  // Aquí es donde debe estar definida la variable $conn

        if ($stmt) {
            $stmt->bind_param("isss", $valor, $sonido, $HoraFecha, $nombre_instrumento);
            if ($stmt->execute()) {
                echo "Datos insertados correctamente";
            } else {
                echo "Error en la inserción: " . $stmt->error;
            }
            $stmt->close();
        } else {
            echo "Error en la preparación de la consulta: " . $conn->error;
        }
        $conn->close();
    } else {
        echo "No se recibieron datos";
    }
} else {
    echo "Solicitud no válida";
}
?>
