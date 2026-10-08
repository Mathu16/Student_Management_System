import { useState } from "react";
import API from "../services/api";
import CreateStudent from "../components/CreateStudent";
import UpdateStudent from "../components/UpdateStudent";


function AdminDashboard(){

    const [students, setStudents] = useState([]);
    const [selectedStudent, setSelectedStudent] = useState(null);


    const getStudents = async () => {

        try {

            const response = await API.get("/students/");

            setStudents(response.data);

        } 
        catch(error){

            console.log(error);

        }

    };


    const deleteStudent = async (student_id)=>{

        try{

            await API.delete(
                `/students/${student_id}`
            );


            alert("Student deleted successfully");


            getStudents();


        }
        catch(error){

            console.log(error);

            alert("Student deletion failed");

        }

    };


    return(

        <div className="dashboard">


            <h1>
                Admin Dashboard
            </h1>



            {/* Create Student Section */}

            <div className="section-card">

                <CreateStudent 
                    onStudentCreated={getStudents}
                />

            </div>



            {/* View Students Button */}

            <div className="section-card">


                <button onClick={getStudents}>

                    View Students

                </button>


            </div>

            {/* Update Student Section */}

            <div className="section-card">

                <UpdateStudent 
                    student={selectedStudent}
                />

            </div>




            {/* Student List Section */}

            <div className="section-card">


                <h2>
                    Student List
                </h2>



                {

                    students.map((student)=>(


                        <div 
                            key={student.id}
                            className="student-card"
                        >



                            <p>
                                <strong>Name:</strong> {student.full_name}
                            </p>



                            <p>
                                <strong>Email:</strong> {student.email}
                            </p>



                            <div className="action-buttons">


                                <button

                                    onClick={() => 
                                        setSelectedStudent(student)
                                    }

                                >

                                    Update

                                </button>




                                <button

                                    className="delete-btn"

                                    onClick={() => 
                                        deleteStudent(student.id)
                                    }

                                >

                                    Delete

                                </button>



                            </div>



                        </div>


                    ))

                }


            </div>



        </div>

    )

}


export default AdminDashboard;