import joblib
import os
import sys

# Lấy đường dẫn gốc để load model
current_dir = os.path.dirname(os.path.abspath(__file__))
# Đường dẫn đến file model .pkl
MODEL_PATH = os.path.join(current_dir, '..', '..', 'ml_artifacts', 'svc_fake_reviews_model.pkl')

class AIModel:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        """Tải model từ file .pkl"""
        if os.path.exists(MODEL_PATH):
            try:
                self.model = joblib.load(MODEL_PATH)
                print(f"✅ Đã tải model thành công từ: {MODEL_PATH}")
            except Exception as e:
                print(f"❌ Lỗi khi tải model: {e}")
                self.model = None
        else:
            print(f"⚠️ Cảnh báo: Không tìm thấy model tại {MODEL_PATH}")

    def predict(self, text):
        """
        Dự đoán nhãn cho văn bản đầu vào.
        Trả về: (label, confidence_score)
        """
        if not self.model:
            return None, 0.0
        
        # Dự đoán nhãn (Ví dụ: 'OR' hoặc 'CG')
        prediction = self.model.predict([text])[0]
        
        # Dự đoán xác suất (Độ tin cậy)
        proba = self.model.predict_proba([text])
        confidence = max(proba[0]) * 100  # Lấy % cao nhất
        
        return prediction, round(confidence, 2)

# Khởi tạo instance duy nhất để dùng chung (Singleton pattern đơn giản)
ai_model = AIModel()