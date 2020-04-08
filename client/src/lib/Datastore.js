
import Axios from 'axios';
const storeEndpoint = Axios.create ({
    baseURL: 'http://localhost:4000/api/store/',
    timeout: 20000,
    headers: {
        'Content-Type': "application/json"
    }
})


class Datastore {
    
    static async get (){
        return await storeEndpoint.post("get");
    }

    static async send (data){
        console.log(`sending data:`);
        console.log(data);
        await storeEndpoint.post("send", data);
        console.log(`sent data`);
    }

}


export default Datastore;