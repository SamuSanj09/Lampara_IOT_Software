<?php
include 'db.php';

// Obtener la hora actual menos 60 segundos
$datetime = date('Y-m-d H:i:s', strtotime('-1 minute'));

$instrumentos_principales = ['Guitarra', 'Tambor', 'Bateria', 'Caja de haija', 'Charango'];
$instrumentos = array();

foreach ($instrumentos_principales as $instrumento) {
    $sql = "SELECT nombre_instrumento, valor, sonido FROM instrumento WHERE nombre_instrumento = ? AND HoraFecha >= ? ORDER BY HoraFecha DESC LIMIT 1";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $instrumento, $datetime);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $instrumentos[] = $row;
    } else {
        $instrumentos[] = array('nombre_instrumento' => $instrumento, 'valor' => 1, 'sonido' => ''); // Si no hay datos recientes, asumir que no está emitiendo sonido
    }

    $stmt->close();
}

$conn->close();

header('Content-Type: application/json');
echo json_encode($instrumentos);
?>
