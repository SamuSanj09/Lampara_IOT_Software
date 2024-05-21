import { obtenerColorAleatorio } from "./util.js";

export function destruirGrafico(canvasId) {
  const canvas = document.querySelector(`#${canvasId}`);
  if (canvas && canvas.chart) {
    canvas.chart.destroy();
  }
}

export function actualizarColorFondo(estadoLampara) {
  const colorFondo = estadoLampara === 2 ? "#FFD700" : "#708090"; // Oro si está encendido, gris si está apagado
  document.body.style.transition = "background-color 0.5s ease";
  document.body.style.backgroundColor = colorFondo;
}

export function crearGrafico(datos, canvasId, label, dataLabel) {
  const ctx = document.getElementById(canvasId).getContext("2d");
  const chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: datos.map((item) => item.fecha_creacion),
      datasets: [
        {
          label: label,
          data: datos.map((item) => item[dataLabel]),
          borderColor: obtenerColorAleatorio(),
          tension: 0.1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
  document.querySelector(`#${canvasId}`).chart = chart;
}

export function crearHistograma(datos, canvasId, label, dataLabel) {
  const ctx = document.getElementById(canvasId).getContext("2d");
  const chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: datos.map((item) => item.UserID),
      datasets: [
        {
          label: label,
          data: datos.map((item) => item[dataLabel]),
          backgroundColor: datos.map(() => obtenerColorAleatorio()),
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
  document.querySelector(`#${canvasId}`).chart = chart;
}

export function crearGraficoRelacion(datos, canvasId, label) {
  const ctx = document.getElementById(canvasId).getContext("2d");
  const chart = new Chart(ctx, {
    type: "scatter",
    data: {
      datasets: [
        {
          label: label,
          data: datos.map((item) => ({
            x: new Date(item.fecha_creacion),
            y: item.UserID,
          })),
          backgroundColor: obtenerColorAleatorio(),
        },
      ],
    },
    options: {
      scales: {
        x: {
          type: "time",
          time: {
            unit: "day",
          },
          title: {
            display: true,
            text: "Fecha de Creación",
          },
        },
        y: {
          title: {
            display: true,
            text: "UsuarioID",
          },
          beginAtZero: true,
        },
      },
    },
  });
  document.querySelector(`#${canvasId}`).chart = chart;
}

export function crearGraficoVidaUtil(datos, canvasId) {
  const ctx = document.getElementById(canvasId).getContext("2d");
  const chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: datos.map((item) => item.LampID),
      datasets: [
        {
          label: "Horas Restantes",
          data: datos.map((item) => item.HorasRestantes),
          borderColor: obtenerColorAleatorio(),
          tension: 0.1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
  document.querySelector(`#${canvasId}`).chart = chart;

  // Mostrar alerta si alguna lámpara tiene menos del 10% de vida útil
  /*
  datos.forEach((item) => {
    if (item.Estado === "ALERTA: Vida útil menor al 10%") {
      alert(
        `ALERTA: La lámpara ${item.LampID} tiene menos del 10% de vida útil restante.`
      );
    }
  });*/
}
