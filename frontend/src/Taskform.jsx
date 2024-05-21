import  './Taskform.css';

export  function TaskForm(){
return(
    <>    
    <form method="post" encType="multipart/form-data">
        <label> Create Task</label>
        <input id="task"></input>
        <button type="submit">Add</button>
        <a href="/Home">Back to home</a>
    </form>
    </>
)    


}