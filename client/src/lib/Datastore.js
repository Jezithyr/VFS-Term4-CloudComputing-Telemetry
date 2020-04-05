
import Axios from 'axios';
const axios = Axios.create ({
    baseUrl: 'https://localhost:4000/api/store'
})


class Datastore {
    
    static async send (data){
        console.log(`sending data`);
        await axios.post("/send", data);
        console.log(`sent data`);
    }

}


export default Datastore;