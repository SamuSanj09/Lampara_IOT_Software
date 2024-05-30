<?php
include 'db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nombre_instrumento = $_POST['nombre_instrumento'];
    $valor = $_POST['valor'];
    $sonido = $_POST['sonido'];
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
    echo "Solicitud no válida";
}
?>
