import { useContext } from 'react'
import { AdminContext } from './context/AdminContext'
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import { Route, Routes } from 'react-router-dom';
import Employee from './pages/Employee';

function App() {
  const { showSidebar } = useContext(AdminContext);
  
  
  return (
    <div className='bg-gray-100 min-h-screen'>
      <div
        className={`w-[20%] h-screen fixed top-0 left-0 bg-white transition-transform duration-300 z-20 ${
          showSidebar ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        <Sidebar />
      </div>
      <div className={ `transition-all duration-300 ${showSidebar? 'ml-[20%]' : 'w-full'}`}>
        <Navbar />
      </div>
      <div className={`ml-[20%] p-4 transition-all duration-300 ${showSidebar ? 'w-[80%]' : 'w-full'}`}>
        <Routes>
          <Route path="/" element={<Employee />} />
          {/* Add more routes as needed */}
        </Routes>
      </div>
    </div>
  );
}

export default App;
