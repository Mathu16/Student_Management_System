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

        } catch(error){

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

        <div>

            <h1>
                Admin Dashboard
            </h1>

            <CreateStudent onStudentCreated={getStudents} />
            <UpdateStudent student={selectedStudent} />

            <button onClick={getStudents}>
                View Students
            </button>


            <h2>
                Student List
            </h2>


            {
                students.map((student)=>(

                    <div key={student.id}>

                        <p>
                            Name: {student.full_name}
                        </p>

                        <p>
                            Email: {student.email}
                        </p>

                        <button 
                            onClick={() => setSelectedStudent(student)}
                        >
                            Update
                        </button>
                        
                        <button
                            onClick={() => deleteStudent(student.id)}
                        >
                            Delete
                        </button>

                        <hr/>

                    </div>

                ))
            }


        </div>

    )

}


export default AdminDashboard;