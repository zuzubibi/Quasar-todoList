import axios from "axios";

const instance = axios.create({
    baseURL: "http://localhost:8000/"
})

function RequestToken(){
    return instance.get('url');
}

function GetToken(){
    return instance.get('url/getToken');
}

export { RequestToken, GetToken };
