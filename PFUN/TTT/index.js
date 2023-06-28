const fs = require('fs');
const api = require('./api');

async function guardarEnArchivo(nombreArchivo, datos) {
  
    const rutaArchivo = `./salida/${nombreArchivo}.json`;
    const datosJson = JSON.stringify(datos, null, 2);
    await fs.promises.writeFile(rutaArchivo, datosJson);
    console.log(`Archivo ${nombreArchivo}.json generado correctamente.`);
  
}

async function contarLocalesPorCadena() {
  
    const farmacias = await api.obtenerFarmacias();

    const localesPorCadena = farmacias.reduce((contador, farmacia) => {
      const cadena = farmacia.local_nombre.trim();

      contador[cadena] = (contador[cadena] || 0) + 1;

      return contador;
    }, {});

    await guardarEnArchivo('1-locales-por-cadena', localesPorCadena);
  
}

async function contarLocalesPorComuna() {
  try {
    const farmacias = await api.obtenerFarmacias();

    const localesPorComuna = {};

    farmacias.forEach((farmacia) => {
      const comuna = farmacia.comuna_nombre.trim();

      if (!localesPorComuna[comuna]) {
        localesPorComuna[comuna] = 0;
      }

      localesPorComuna[comuna]++;
    });

    await guardarEnArchivo('2-locales-por-comuna', localesPorComuna);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function contarLocalesDespuesDeHora(hora) {
  try {
    const farmacias = await api.obtenerFarmacias();

    const localesDespuesDeHora = farmacias.filter((farmacia) => {
      const horaApertura = new Date(`1970-01-01T${farmacia.funcionamiento_hora_apertura}`);
      const horaConsulta = new Date(`1970-01-01T${hora}`);

      return horaApertura > horaConsulta;
    });

    console.log('Cantidad de locales que abren después de', hora, ':', localesDespuesDeHora.length);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function agruparLocalesPorComunaYCadena() {
  try {
    const farmacias = await api.obtenerFarmacias();

    const localesPorComunaYCadena = {};

    farmacias.forEach((farmacia) => {
      const comuna = farmacia.comuna_nombre.trim();
      const cadena = farmacia.local_nombre.trim();
      const localId = farmacia.local_id;

      if (!localesPorComunaYCadena[comuna]) {
        localesPorComunaYCadena[comuna] = {};
      }

      if (!localesPorComunaYCadena[comuna][cadena]) {
        localesPorComunaYCadena[comuna][cadena] = [];
      }

      localesPorComunaYCadena[comuna][cadena].push(localId);
    });

    await guardarEnArchivo('4-locales-por-comuna-y-cadena', localesPorComunaYCadena);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function cadenaMasPresentePorComuna() {
    try {
      const farmacias = await api.obtenerFarmacias();
  
      const resultado = {};
  
      farmacias.forEach((farmacia) => {
        const comuna = farmacia.comuna_nombre.trim();
        const cadena = farmacia.local_nombre.trim();
  
        if (!resultado[comuna]) {
          resultado[comuna] = {};
        }
  
        if (!resultado[comuna][cadena]) {
          resultado[comuna][cadena] = 0;
        }
  
        resultado[comuna][cadena]++;
      });
  
      for (const comuna in resultado) {
        const cadenas = resultado[comuna];
        let maxCantidad = 0;
        let cadenaMasPresente = '';
  
        for (const cadena in cadenas) {
          const cantidad = cadenas[cadena];
  
          if (cantidad > maxCantidad) {
            maxCantidad = cantidad;
            cadenaMasPresente = cadena;
          }
        }
  
        resultado[comuna] = cadenaMasPresente;
      }
  
      console.log('Cadena más presente por comuna:', resultado);
    } catch (error) {
      console.error('Error:', error.message);
    }
  }
  
  

async function comunaConMasFarmacias() {
  try {
    const farmacias = await api.obtenerFarmacias();

    const cantidadFarmaciasPorComuna = {};

    farmacias.forEach((farmacia) => {
      const comuna = farmacia.comuna_nombre.trim();

      if (!cantidadFarmaciasPorComuna[comuna]) {
        cantidadFarmaciasPorComuna[comuna] = 0;
      }

      cantidadFarmaciasPorComuna[comuna]++;
    });

    const comunaConMasFarmacias = Object.keys(cantidadFarmaciasPorComuna).reduce((comunaMax, comuna) => {
      if (!comunaMax || cantidadFarmaciasPorComuna[comuna] > cantidadFarmaciasPorComuna[comunaMax]) {
        return comuna;
      }
      return comunaMax;
    }, null);

    console.log('Comuna con mayor cantidad de farmacias:', comunaConMasFarmacias);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function promedioHorasFuncionamientoCadena() {
  try {
    const farmacias = await api.obtenerFarmacias();

    const horasPorCadena = farmacias.reduce((acumulador, farmacia) => {
      const cadena = farmacia.local_nombre.trim();
      const horaApertura = new Date(`1970-01-01T${farmacia.funcionamiento_hora_apertura}`);
      const horaCierre = new Date(`1970-01-01T${farmacia.funcionamiento_hora_cierre}`);
      const duracionHoras = (horaCierre - horaApertura) / 3600000; // Convertir a horas

      if (!acumulador[cadena]) {
        acumulador[cadena] = [];
      }

      acumulador[cadena].push(duracionHoras);

      return acumulador;
    }, {});

    const promedioHorasPorCadena = {};

    for (const cadena in horasPorCadena) {
      const horas = horasPorCadena[cadena];
      const promedio = horas.reduce((sum, hora) => sum + hora, 0) / horas.length;
      promedioHorasPorCadena[cadena] = promedio;
    }

    await guardarEnArchivo('7-promedio-horas-funcionamiento-cadena', promedioHorasPorCadena);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function farmaciaMasAislada() {
  try {
    const farmacias = await api.obtenerFarmacias();

    const farmaciaMasAislada = farmacias.reduce((farmaciaAislada, farmacia) => {
      const latitud = parseFloat(farmacia.local_lat);
      const longitud = parseFloat(farmacia.local_lng);
      const distancia = Math.sqrt(latitud ** 2 + longitud ** 2);

      if (!farmaciaAislada || distancia > farmaciaAislada.distancia) {
        farmaciaAislada = {
          id: farmacia.local_id,
          nombre: farmacia.local_nombre,
          distancia: distancia
        };
      }

      return farmaciaAislada;
    }, null);

    console.log('Farmacia más aislada del país:', farmaciaMasAislada);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

async function ejecutarPrograma() {
  await contarLocalesPorCadena();
  await contarLocalesPorComuna();
  await contarLocalesDespuesDeHora('18:00:00');
  await agruparLocalesPorComunaYCadena();
  await cadenaMasPresentePorComuna();
  await comunaConMasFarmacias();
  await promedioHorasFuncionamientoCadena();
  await farmaciaMasAislada();
}

ejecutarPrograma();
