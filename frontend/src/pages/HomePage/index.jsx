import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import authApi from '../../api/auth';
import styles from './HomePage.module.css'; // Dùng lại style cũ hoặc tạo mới

const HomePage = () => {
  const navigate = useNavigate();
  const userString = localStorage.getItem('user_info');
  const user = userString ? JSON.parse(userString) : null;

  const handleLogout = () => {
    authApi.logout();
    navigate('/login');
  };

  return (
    <div className={styles.pageContainer}>
      <header style={{ marginBottom: '40px', borderBottom: '1px solid #ddd', paddingBottom: '10px' }}>
        {user ? (
          <div>
            <span>Xin chào, <b>{user.username}</b> ({user.role}) </span>
            <button onClick={handleLogout} style={{marginLeft:'10px', cursor:'pointer'}}>Đăng xuất</button>
          </div>
        ) : (
          <div>
            <Link to="/login" style={{marginRight:'15px'}}>Đăng nhập</Link>
            <Link to="/register">Đăng ký</Link>
          </div>
        )}
      </header>

      <h1>🏠 TRANG CHỦ HỆ THỐNG</h1>
      <p>Chào mừng bạn đến với hệ thống AI E-commerce.</p>

      <div style={{marginTop: '30px', display: 'flex', gap: '20px', justifyContent: 'center'}}>
        {/* Link dẫn đến các trang chức năng */}
        <Link to="/dashboard/test" style={{
            padding: '15px 30px', background: '#3498db', color: 'white', 
            textDecoration: 'none', borderRadius: '5px', fontWeight: 'bold'
        }}>
           🔍 Vào công cụ Test Review
        </Link>

        {user?.role === 'admin' && (
            <Link to="/admin" style={{
                padding: '15px 30px', background: '#e74c3c', color: 'white', 
                textDecoration: 'none', borderRadius: '5px', fontWeight: 'bold'
            }}>
               🛡️ Vào trang Admin
            </Link>
        )}
      </div>
    </div>
  );
};

export default HomePage;