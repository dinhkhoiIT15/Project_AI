import React from 'react';
import { Routes, Route } from 'react-router-dom';
import HomePage from '../pages/HomePage';
import LoginPage from "../pages/Auth/LoginPage";
import RegisterPage from "../pages/Auth/RegisterPage";
import FakeReviewPage from '../pages/FakeReviewPage'; // Import trang cũ (đã đổi tên)
import AdminDashboard from '../pages/AdminDashboard'; // Import trang Admin
import PrivateRoute from '../components/PrivateRoute'; // Import bảo vệ

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      {/* Sau này thêm: <Route path="/history" element={<HistoryPage />} /> */}
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />

      {/* 2. PROTECTED ROUTES (Phải đăng nhập mới vào được) */}
      <Route element={<PrivateRoute />}>
         {/* Cả Admin và Customer đều vào được */}
         <Route path="/dashboard/test" element={<FakeReviewPage />} />
      </Route>

      {/* 3. ADMIN ROUTES (Chỉ Admin mới vào được) */}
      <Route element={<PrivateRoute allowedRoles={['admin']} />}>
         <Route path="/admin" element={<AdminDashboard />} />
      </Route>
    </Routes>
  );
};

export default AppRoutes;