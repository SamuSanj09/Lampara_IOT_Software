document.addEventListener('DOMContentLoaded', function() {
    // Variables para almacenar las instancias de los gráficos
    let Grafico1, Grafico2, Grafico3, Grafico4;

    // Función para obtener los datos del servidor
    function obtenerDatos() {
        const nombre_instrumento = document.getElementById('nombre_instrumento').value; // Obtener el LampID del campo de entrada
        
        // Realizar la solicitud al servidor con el LampID proporcionado
        fetch(`../php/obtener_datos.php?nombre_instrumento=${nombre_instrumento}`)
        .then(response => response.json())
        .then(data => {
            // Destruir gráficos existentes antes de crear nuevos
            if (Grafico1) Grafico1.destroy();   
            if (Grafico2) Grafico2.destroy();
            if (Grafico3) Grafico3.destroy();
            if (Grafico4) Grafico4.destroy();

            

            // Generar los gráficos con los datos recibidos
            const ctxLamp = document.getElementById('Grafico1');
            const ctxTemp = document.getElementById('Grafico2');
            const ctxLamp2 = document.getElementById('Grafico3');
            const ctxTemp2 = document.getElementById('Grafico4');
            
            Grafico1 = new Chart(ctxLamp, {
                type: 'line',
                data: {
                    labels: data.Grafico1.map(item => item.Hora),
                    datasets: [{
                        label: 'Hora vs Frecuencia',
                        data: data.Grafico1.map(item => item.Frecuencia),
                    }]
                },
                options: {}
            });

            Grafico2 = new Chart(ctxTemp, {
                type: 'bar',
                data: {
                    labels: data.Grafico2.map(item => item.valor1),
                    datasets: [{
                        label: 'Valor vs Frecuencia',
                        data: data.Grafico2.map(item => item.Frecuencia),
                    }]
                },
                options: {}
            });

            Grafico3 = new Chart(ctxLamp2, {
                type: 'pie',
                data: {
                    labels: data.Grafico3.map(item => item.valor2),
                    datasets: [{
                        label: 'Valores y su Frecuencia',
                        data: data.Grafico3.map(item => item.Frecuencia2),
                    }]
                },
                options: {}
            });

            Grafico4 = new Chart(ctxTemp2, {
                type: 'line',
                data: {
                    labels: data.Grafico4.map(item => item.valor3),
                    datasets: [{
                        label: 'Fecha Creacion y Temp - Histograma',
                        data: data.Grafico4.map(item => item.id_actual),
                    }]
                },
                options: {}
            });
        })
        .catch(error => console.error('Error al obtener los datos:', error));
    }

    
    document.getElementById('formulario_lamp_id').addEventListener('submit', function(event) {
        event.preventDefault(); 
        obtenerDatos();
    });

    // Llamar intervalo de tiempo
    setInterval(obtenerDatos, 5000);
});