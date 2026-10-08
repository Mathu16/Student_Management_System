import { useState } from "react";
import API from "../services/api";


function Login(){

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");


    const handleLogin = async () => {

        try {

            const formData = new FormData();

            formData.append("username", username);
            formData.append("password", password);


            const response = await API.post(
                "/auth/login",
                formData
            );


            localStorage.setItem(
                "token",
                response.data.access_token
            );


            localStorage.setItem(
                "role",
                response.data.role
            );


            console.log("Login successful");


        } catch(error){

            console.log(error);

        }

    };


    return(

        <div>

            <h1>
                Student Management System
            </h1>


            <h2>
                Login
            </h2>


            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e)=>setUsername(e.target.value)}
            />


            <br/><br/>


            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e)=>setPassword(e.target.value)}
            />


            <br/><br/>


            <button onClick={handleLogin}>
                Login
            </button>


        </div>

    )

}


export default Login;