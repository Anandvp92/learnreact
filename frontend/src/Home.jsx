import React from 'react';
import axios from 'axios';
import './Home.css';
import { useState, useEffect } from 'react';

export function Home() {
  const [tasks, setTasks] = useState([]);

  const listTask = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:4000/listall");
      setTasks(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  const deleteTask = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:4000/deletetodo/${id}`);
      // Refresh task list after deletion
      listTask();
    } catch (error) {
      console.log("Something went wrong", error);
    }
  };

  useEffect(() => {
    // Fetch tasks on component mount
    listTask();

    // Refresh tasks every 1000ms
    const intervalId = setInterval(listTask, 1000);

    // Cleanup function to clear interval
    return () => clearInterval(intervalId);
  }, []);

  return (
    <>  
      <div id='tablecontainer'>
        <table>
          <thead>
            <tr>
              <th>SI NO</th>
              <th>Task</th>
              <th>Created Date</th>
              <th>Updated Date</th>
              <th>Task Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {tasks.length === 0 ? (
              <tr key="notask">
                <td colSpan={6}>There is no task available</td>         
              </tr>
            ) : (
              tasks.map((task, index) => (
                <React.Fragment key={`task-fragment-${index}`}>
                  <tr key={`maintask-${index}`}>
                    <td>{task.id}</td>
                    <td>{task.task}</td>
                    <td>{task["created time"]}</td>
                    <td>{task["updated date"]}</td>
                    <td>{task.status === 0 ? "Not Completed" : "Completed"}</td>
                    <td id='actionrow'>
                      <button id="deletebtn" onClick={() => deleteTask(task.id)}>Delete Task</button> 
                      <button id='editbtn'>Edit Task</button>
                    </td>       
                  </tr>
                  <tr key={`createtask-${index}`}>
                    <td colSpan={6}><button id='createtaskbtn'><a href='/Createtask'>Create New Task</a></button></td>
                  </tr>
                </React.Fragment>
              ))
            )}
          </tbody>
        </table>
      </div> 
    </>
  );
}
