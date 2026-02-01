import React from 'react';
// Import styles từ file module.
// React sẽ tự đổi tên class thành dạng: ResultCard_container__xyz123 (không bao giờ trùng)
import styles from './ResultCard.module.css'; 

const ResultCard = ({ result }) => {
  if (!result) return null;

  const isFake = result.label === 'CG';

  return (
    // Kết hợp class chung (.container) và class động (.fake/.real)
    <div className={`${styles.container} ${isFake ? styles.fake : styles.real}`}>
      <h3 className={styles.title}>
        {isFake ? '🚫 FAKE REVIEW' : '✅ REAL REVIEW'}
      </h3>
      <p>Độ tin cậy: <strong>{result.confidence}%</strong></p>
    </div>
  );
};

export default ResultCard;