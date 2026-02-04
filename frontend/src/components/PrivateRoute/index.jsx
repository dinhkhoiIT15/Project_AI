import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const PrivateRoute = ({ allowedRoles }) => {
  // 1. Lấy thông tin User từ LocalStorage
  const userString = localStorage.getItem('user_info');
  const token = localStorage.getItem('access_token');
  const user = userString ? JSON.parse(userString) : null;

  // 2. Nếu không có Token -> Đuổi về trang Login
  if (!token || !user) {
    return <Navigate to="/login" replace />;
  }

  // 3. Nếu có yêu cầu Role cụ thể (vd: admin) mà User không có -> Chặn
  if (allowedRoles && !allowedRoles.includes(user.role)) {
    alert("Bạn không có quyền truy cập trang này!");
    return <Navigate to="/" replace />; // Hoặc trang 403
  }

  // 4. Nếu thỏa mãn -> Cho đi tiếp (Render component con)
  return <Outlet />;
};

export default PrivateRoute;