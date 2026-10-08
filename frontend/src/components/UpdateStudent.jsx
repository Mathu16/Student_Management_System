import { useState, useEffect } from "react";
import API from "../services/api";


function UpdateStudent({student}){


    const [updatedStudent, setUpdatedStudent] = useState({

        full_name:"",
        email:"",
        phone:""

    });


    useEffect(()=>{

        if(student){

            setUpdatedStudent({

                full_name: student.full_name,
                email: student.email,
                phone: student.phone

            });

        }

    },[student]);



    const handleChange = (e)=>{

        setUpdatedStudent({

            ...updatedStudent,

            [e.target.name]: e.target.value

        });

    };



    const handleUpdate = async()=>{


        try{


            const response = await API.put(

                `/students/${student.id}`,

                updatedStudent

            );


            console.log(response.data);


            alert("Student updated successfully");


        }

        catch(error){

            console.log(error);

            alert("Student update failed");

        }


    };



    return(

        <div>


            <h2>
                Update Student
            </h2>


            {
                student && (

                <div>


                    <input

                        name="full_name"

                        value={updatedStudent.full_name}

                        onChange={handleChange}

                    />


                    <br/><br/>


                    <input

                        name="email"

                        value={updatedStudent.email}

                        onChange={handleChange}

                    />


                    <br/><br/>


                    <input

                        name="phone"

                        value={updatedStudent.phone}

                        onChange={handleChange}

                    />


                    <br/><br/>


                    <button onClick={handleUpdate}>

                        Update Student

                    </button>


                </div>

                )

            }


        </div>

    )

}


export default UpdateStudent;