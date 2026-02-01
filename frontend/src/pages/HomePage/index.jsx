import React, { useState } from 'react';
import axiosClient from '../../api/axiosClient'; 
import ResultCard from '../../components/ResultCard'; // Import từ folder mới
import styles from './HomePage.module.css'; // Import CSS Module

const HomePage = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!text.trim()) return alert("Vui lòng nhập nội dung!");
    setLoading(true);
    try {
      const response = await axiosClient.post('/predict', { text });
      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Lỗi kết nối Server!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.pageContainer}>
      <h1>AI Review Detector</h1>
      
      <textarea
        className={styles.textArea}
        rows="6"
        placeholder="Nhập review tiếng Anh..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      
      <button 
        className={styles.checkButton}
        onClick={handleSubmit} 
        disabled={loading}
      >
        {loading ? 'Đang phân tích...' : '🔍 Kiểm tra ngay'}
      </button>

      <ResultCard result={result} />
    </div>
  );
};

export default HomePage;