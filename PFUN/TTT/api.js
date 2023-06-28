const axios = require('axios');

async function obtenerFarmacias() {
  
    const response = await axios.get('https://andreshoward.com/pharmacies');
    return response.data;
  
}

module.exports = {
  obtenerFarmacias
};
