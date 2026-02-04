import React, { useState, useEffect} from 'react';
import axiosClient from '../../api/axiosClient'; 
import ResultCard from '../../components/ResultCard'; // Import từ folder mới
import HistoryList from "../../components/HistoryList";
import styles from './FakeReviewPage.module.css'; // Import CSS Module

const HomePage = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  // State mới để chứa danh sách lịch sử
  const [history, setHistory] = useState([]);

  // useEffect: Chạy 1 lần duy nhất khi trang vừa mở
  useEffect(() => {
    fetchHistory();
  }, []);

  const handleSubmit = async () => {
    if (!text.trim()) return alert("Vui lòng nhập nội dung!");
    setLoading(true);
    try {
      // 1. Gửi đi dự đoán
      const response = await axiosClient.post('/predict', { text });
      setResult(response.data);

      // 2. Dự đoán xong thì tải lại lịch sử ngay lập tức
      fetchHistory();
    } catch (error) {
      console.error(error);
      alert("Lỗi kết nối Server!");
    } finally {
      setLoading(false);
    }
  };

  // Hàm tải lịch sử từ Backend
  const fetchHistory = async () => {
    try {
      const response = await axiosClient.get('/history');
      setHistory(response.data);
    } catch (error) {
      console.error("Không thể tải lịch sử:", error);
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

      {/* Kết quả hiện tại */}
      <ResultCard result={result} />
      {/* --- THÊM DÒNG NÀY VÀO ĐỂ HIỂN THỊ LỊCH SỬ --- */}
      <HistoryList historyData={history} />
    </div>
  );
};

export default HomePage;