import axios from "axios";

function registerUser(){
    const url = 'http://localhost:3000/singup';
    return axios.post(url);
}

export { registerUser};