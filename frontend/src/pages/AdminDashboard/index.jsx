import React from 'react';

const AdminDashboard = () => {
  return (
    <div className="container" style={{textAlign: 'center', marginTop: '50px'}}>
      <h1 style={{color: '#e74c3c'}}>🛡️ ADMIN DASHBOARD</h1>
      <p>Chào mừng quản trị viên.</p>
      <div style={{marginTop: '20px', padding: '20px', background: '#fff', borderRadius: '8px'}}>
        <h3>Thống kê hệ thống</h3>
        <p>User đang hoạt động: 2</p>
        <p>Tổng số review đã check: 15</p>
        {/* Sau này thêm nút Quản lý User, Tạo Sản phẩm ở đây */}
      </div>
    </div>
  );
};

export default AdminDashboard;