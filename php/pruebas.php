<?php

include 'conectar_bd.php';

$lampID = isset($_GET['lampID']) ? $_GET['lampID'] : 'Lamp01'; // Default a 'Lamp01' si no se proporciona

$consultas = [
    'LampOnOff' => "SELECT fecha_creacion, LampOnOff as Frecuencia FROM t_iotlampv0 WHERE LampID = ? GROUP BY LampOnOff ORDER BY fecha_creacion ASC",
    'temp_value' => "SELECT fecha_creacion, temp_value as Frecuencia FROM t_iotlampv0 WHERE LampID = ? GROUP BY temp_value ORDER BY fecha_creacion ASC",
    'temp_int' => "SELECT fecha_creacion, temp_int as Frecuencia FROM t_iotlampv0 WHERE LampID = ? GROUP BY temp_int ORDER BY fecha_creacion ASC",
    'sep_point' => "SELECT fecha_creacion, sep_point as Frecuencia FROM t_iotlampv0 WHERE LampID = ? GROUP BY sep_point ORDER BY fecha_creacion ASC",
    'ultimoLampOnOff' => "SELECT LampOnOff FROM t_iotlampv0 WHERE LampID = ? ORDER BY fecha_creacion DESC LIMIT 1",
    'histograma_usuario' => "SELECT UserID, COUNT(*) as Frecuencia FROM t_iotlampv0 GROUP BY UserID",
    'relacion_fecha_usuario' => "SELECT fecha_creacion, UserID FROM t_iotlampv0 ORDER BY fecha_creacion ASC",
    'histograma_usuario_lamp' => "SELECT UserID, COUNT(DISTINCT LampID) as NumLamps FROM t_iotlampv0 GROUP BY UserID",
    'consumo_total' => "SELECT LampID, SUM(sep_point * 0.84) as ConsumoTotalBs FROM t_iotlampv0 GROUP BY LampID",
    'vida_util' => "SELECT LampID, 1000 - SUM(sep_point) as HorasRestantes, 
                    CASE WHEN 1000 - SUM(sep_point) < 100 THEN 'ALERTA: Vida útil menor al 10%' ELSE 'OK' END as Estado 
                    FROM t_iotlampv0 
                    WHERE LampID = ? 
                    GROUP BY LampID"
];

$resultados = [];
foreach ($consultas as $key => $sql) {
    $stmt = $conn->prepare($sql);

    // Verifica si la consulta necesita el parámetro LampID
    if (in_array($key, ['LampOnOff', 'temp_value', 'temp_int', 'sep_point', 'ultimoLampOnOff', 'vida_util'])) {
        $stmt->bind_param("s", $lampID);
    }

    $stmt->execute();
    $resultado = $stmt->get_result();
    $datos = [];
    while($fila = $resultado->fetch_assoc()) {
        $datos[] = $fila;
    }
    $resultados[$key] = $datos;
}

$conn->close();

echo json_encode($resultados, JSON_PRETTY_PRINT);

?>
