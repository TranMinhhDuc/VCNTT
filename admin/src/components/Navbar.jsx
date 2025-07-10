import { faBars } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import React, { useContext } from 'react'
import { AdminContext } from '../context/AdminContext';

const Navbar = () => {
  const { setShowSidebar } = useContext(AdminContext);
  return (
    <div className='bg-white shadow-md py-2 w-full'>
        <div className='flex justify-between items-center px-4 md:px-8'>
            <FontAwesomeIcon 
              icon={faBars}  
              className='text-lg ml-5 cursor-pointer'
              onClick={() => setShowSidebar(prev => !prev)}
            />
            <button 
              className='bg-blue-500 hover:bg-red-400 text-white py-1 px-3 rounded-sm mr-7'
            >
              Đăng xuất
            </button>
        </div>
      
    </div>
  )
}

export default Navbar
