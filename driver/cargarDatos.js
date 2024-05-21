import {
  destruirGrafico,
  crearGrafico,
  crearHistograma,
  crearGraficoRelacion,
  crearGraficoVidaUtil,
  actualizarColorFondo,
} from "./grafico.js";

export function cargarDatos() {
  const lampID = document.getElementById("lampIDInput").value;
  const userID = document.getElementById("userIDInput").value;
  fetch(`../php/obtener_datos.php?lampID=${lampID}&userID=${userID}`)
    .then((response) => response.json())
    .then((data) => {
      // Destruir gráficos existentes
      destruirGrafico("lampOnOffChart");
      destruirGrafico("tempValueChart");
      destruirGrafico("tempIntChart");
      destruirGrafico("sepPointChart");
      destruirGrafico("histogramaUsuarioChart");
      destruirGrafico("relacionFechaUsuarioChart");
      destruirGrafico("histogramaUsuarioLampChart");
      destruirGrafico("consumoTotalChart");
      destruirGrafico("vidaUtilChart");

      // Crear nuevos gráficos
      crearGrafico(
        data.LampOnOff,
        "lampOnOffChart",
        "Lamp On/Off Status",
        "Frecuencia"
      );
      crearGrafico(
        data.temp_value,
        "tempValueChart",
        "Temperature Values",
        "Frecuencia"
      );
      crearGrafico(
        data.temp_int,
        "tempIntChart",
        "Internal Temperature",
        "Frecuencia"
      );
      crearGrafico(
        data.sep_point,
        "sepPointChart",
        "Set Point Values",
        "Frecuencia"
      );
      crearHistograma(
        data.histograma_usuario,
        "histogramaUsuarioChart",
        "Frecuencia vs UsuarioID",
        "Frecuencia"
      );
      crearGraficoRelacion(
        data.relacion_fecha_usuario,
        "relacionFechaUsuarioChart",
        "Fecha de Creación vs UsuarioID"
      );
      crearHistograma(
        data.histograma_usuario_lamp,
        "histogramaUsuarioLampChart",
        "UsuarioID vs LampID",
        "NumLamps"
      );
      crearHistograma(
        data.consumo_total,
        "consumoTotalChart",
        "Consumo Total (Bs) vs LampID",
        "ConsumoTotalBs"
      );
      crearGraficoVidaUtil(data.vida_util, "vidaUtilChart");

      // Actualizar el color de fondo en función del último valor de LampOnOff
      if (data.ultimoLampOnOff.length > 0) {
        actualizarColorFondo(data.ultimoLampOnOff[0]);
      }
    })
    .catch((error) => console.error("Error al cargar los datos:", error));
}
