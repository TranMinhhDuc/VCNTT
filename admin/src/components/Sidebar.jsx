import React from 'react'

const Sidebar = () => {
  return (
    <div className='bg-white shadow-md h-screen w-full p-4 flex flex-col justify-center'>
      <h2 className='text-xl font-bold mb-4'>Quản lý</h2>
      <ul className='space-y-2'>
        <li className='hover:bg-gray-200 p-2 rounded'>Dashboard</li>
        <li className='hover:bg-gray-200 p-2 rounded'>Nhân viên</li>
        <li className='hover:bg-gray-200 p-2 rounded'>Phòng ban</li>
        <li className='hover:bg-gray-200 p-2 rounded'>Chức vụ</li>
        <li className='hover:bg-gray-200 p-2 rounded'>Báo cáo</li>
      </ul>
    </div>
  )
}

export default Sidebar
