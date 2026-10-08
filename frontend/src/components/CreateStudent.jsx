import { useState } from "react";
import API from "../services/api";

function CreateStudent({onStudentCreated}){

    const [student, setStudent] = useState({

        full_name:"",
        email:"",
        password:"",
        phone:""

    });


    const handleChange = (e)=>{

        setStudent({

            ...student,

            [e.target.name]: e.target.value

        });

    };

    const handleSubmit = async (e)=>{

    e.preventDefault();

    try{

        const response = await API.post(
            "/students/",
            student
        );


        console.log(response.data);


        alert("Student created successfully");

        onStudentCreated();


    }
    catch(error){

        console.log(error);

        alert("Student creation failed");

    }

};



    return(

        <div>

            <h2>
                Create Student
            </h2>


            <input
                name="full_name"
                placeholder="Full Name"
                value={student.full_name}
                onChange={handleChange}
            />


            <br/><br/>


            <input
                name="email"
                placeholder="Email"
                value={student.email}
                onChange={handleChange}
            />


            <br/><br/>


            <input
                name="password"
                type="password"
                placeholder="Password"
                value={student.password}
                onChange={handleChange}
            />


            <br/><br/>


            <input
                name="phone"
                placeholder="Phone"
                value={student.phone}
                onChange={handleChange}
            />


            <br/><br/>


            <button onClick={handleSubmit}>
                Create Student
            </button>


        </div>

    )

}


export default CreateStudent;