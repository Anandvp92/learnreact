import React, { useEffect ,useState} from 'react';
import '../components/Home.css';


export function Home() {
    let [task,UseTask]=useState("Hello")

  useEffect(() => {
    const getnotes = async () => {
      try {
        let response = await fetch('http://127.0.0.1:4000/listall/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        let data = await response.json();
        console.log(data);
        UseTask(data)

      } catch (error) {
        console.error('Fetch error:', error);
      }
    };
    
    getnotes();
  }, []); // The empty dependency array ensures this runs only once after the initial render

  return (
    <>
   <table>
  
  <tbody>

  <tr>
    <th>SI NO</th>
    <th>Task</th>
    <th>Updated Date</th>
    <th>Created Date</th>
    <th>Status</th>
    <th>Action</th>
  </tr>
  <tr>
    <td>{task[0]["id"]}</td>
    <td>{task[0]["task"]}</td>
    <td>{task[0]["created time"]}</td>
    <td>{task[0]["updated date"]}</td>
    <td>{task[0]["status"]?"Done":"Not Done"}</td>
    <td style={{"display":"flex" ,"gap":"25px" ,"justifyContent":"space-evenly"}}><button><a>Edit</a></button> <button><a>Delete</a></button></td>
  </tr>
  </tbody>
</table>
    </>
  );
}
