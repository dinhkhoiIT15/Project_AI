import React from 'react';
import styles from './HistoryList.module.css';

const HistoryList = ({ historyData }) => {
  // Nếu chưa có lịch sử thì không hiện gì hoặc hiện thông báo
  if (!historyData || historyData.length === 0) {
    return <div className={styles.historyContainer}><p style={{textAlign:'center', color:'#999'}}>Chưa có lịch sử kiểm tra.</p></div>;
  }

  return (
    <div className={styles.historyContainer}>
      <h3 className={styles.heading}>⏳ Lịch sử kiểm tra gần đây</h3>
      
      <div className={styles.listWrapper}>
        {historyData.map((item) => {
          const isFake = item.label === 'CG';
          return (
            <div 
              key={item.id} 
              className={`${styles.item} ${isFake ? styles.fakeItem : styles.realItem}`}
            >
              <div className={styles.headerRow}>
                <span style={{ color: isFake ? '#c0392b' : '#27ae60' }}>
                  {isFake ? '🚫 FAKE' : '✅ REAL'} ({item.confidence}%)
                </span>
                <span style={{ color: '#999', fontSize: '0.8rem' }}>
                  {item.created_at}
                </span>
              </div>
              <p className={styles.textPreview}>{item.text}</p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default HistoryList;