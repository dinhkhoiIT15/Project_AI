import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import authApi from '../../api/auth';
import styles from './Auth.module.css';

const LoginPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ username: '', password: '' });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const res = await authApi.login(formData);
      
      // 1. Lưu Token và Info vào LocalStorage
      localStorage.setItem('access_token', res.data.token);
      localStorage.setItem('user_info', JSON.stringify(res.data.user));
      
      alert("Đăng nhập thành công!");
      
      // 2. Chuyển hướng về trang chủ
      navigate('/'); 
      window.location.reload(); // Reload để cập nhật trạng thái login (tạm thời)
      
    } catch (err) {
      setError(err.response?.data?.error || "Đăng nhập thất bại");
    }
  };

  return (
    <div className={styles.authContainer}>
      <h2 className={styles.title}>Đăng Nhập</h2>
      {error && <p className={styles.error}>{error}</p>}
      
      <form onSubmit={handleSubmit}>
        <div className={styles.inputGroup}>
          <label>Username</label>
          <input 
            type="text" name="username" required
            className={styles.input}
            onChange={handleChange}
          />
        </div>
        <div className={styles.inputGroup}>
          <label>Password</label>
          <input 
            type="password" name="password" required
            className={styles.input}
            onChange={handleChange}
          />
        </div>
        <button type="submit" className={styles.button}>Login</button>
      </form>
      
      <Link to="/register" className={styles.link}>Chưa có tài khoản? Đăng ký ngay</Link>
    </div>
  );
};

export default LoginPage;