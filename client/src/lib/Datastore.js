
import Axios from 'axios';
const axios = Axios.create ({
    baseURL: 'http://localhost:4000/api/store/',
    timeout: 20000
})


class Datastore {
    
    static async send (data){
        console.log(`sending data:`);
        console.log(data);
        await axios.post("send", data);
        console.log(`sent data`);
    }

}


export default Datastore;