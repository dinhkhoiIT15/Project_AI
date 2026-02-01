import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!text) return alert("Vui lòng nhập nội dung!");

    try {
      // Gọi API
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        text,
      });
      setResult(response.data);
    } catch (error) {
      alert("Lỗi kết nối hoặc lỗi Server!");
      console.error(error);
    }
  };

  return (
    <div className="container">
      <h2>Test AI Review</h2>

      {/* Ô Input */}
      <textarea
        rows="5"
        placeholder="Nhập review tiếng Anh..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      {/* Nút Submit */}
      <button onClick={handleSubmit}>Kiểm tra ngay</button>

      {/* Kết quả đơn giản */}
      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>
            Kết quả: {result.label === "CG" ? "FAKE (Giả)" : "REAL (Thật)"}
          </h3>
          <p>Độ tin cậy: {result.confidence}%</p>
        </div>
      )}
    </div>
  );
}

export default App;
