import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import authApi from '../../api/auth';
import styles from './Auth.module.css';

const RegisterPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    try {
      // Gọi API đăng ký
      await authApi.register(formData);
      alert("Đăng ký thành công! Vui lòng đăng nhập.");
      navigate('/login'); // Chuyển sang trang login
    } catch (err) {
      setError(err.response?.data?.error || "Đăng ký thất bại");
    }
  };

  return (
    <div className={styles.authContainer}>
      <h2 className={styles.title}>Đăng Ký User</h2>
      {error && <p className={styles.error}>{error}</p>}
      
      <form onSubmit={handleSubmit}>
        <div className={styles.inputGroup}>
          <label>Username</label>
          <input type="text" name="username" required className={styles.input} onChange={handleChange} />
        </div>
        <div className={styles.inputGroup}>
          <label>Email</label>
          <input type="email" name="email" required className={styles.input} onChange={handleChange} />
        </div>
        <div className={styles.inputGroup}>
          <label>Password</label>
          <input type="password" name="password" required className={styles.input} onChange={handleChange} />
        </div>
        <button type="submit" className={styles.button}>Register</button>
      </form>

      <Link to="/login" className={styles.link}>Đã có tài khoản? Đăng nhập</Link>
    </div>
  );
};

export default RegisterPage;