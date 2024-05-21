import './App.css';
import { Home } from './Home';
import { TaskForm } from './Taskform';
import { BrowserRouter , Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/Home' element={<Home/>} />
        <Route path='/CreateTask' element={<TaskForm/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
