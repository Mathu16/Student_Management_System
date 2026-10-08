import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";


function Login(){

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();



    const handleLogin = async () => {

        try {

            const formData = new FormData();

            formData.append(
                "username",
                username
            );

            formData.append(
                "password",
                password
            );



            const response = await API.post(
                "/auth/login",
                formData
            );



            // Save JWT token

            localStorage.setItem(
                "token",
                response.data.access_token
            );



            // Save user role

            localStorage.setItem(
                "role",
                response.data.role
            );



            alert("Login successful");



            // Redirect based on user role

            if(response.data.role === "admin"){

                navigate("/admin");

            }
            else if(response.data.role === "student"){

                navigate("/student");

            }



        }

        catch(error){

            console.log(error);

            alert("Login failed");

        }

    };



    return(

        <div className="login-page">


            <div className="login-card">


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

                    onChange={(e)=>
                        setUsername(e.target.value)
                    }

                />



                <br/><br/>



                <input

                    type="password"

                    placeholder="Password"

                    value={password}

                    onChange={(e)=>
                        setPassword(e.target.value)
                    }

                />



                <br/><br/>



                <button
                    onClick={handleLogin}
                >

                    Login

                </button>



            </div>


        </div>

    )

}


export default Login;