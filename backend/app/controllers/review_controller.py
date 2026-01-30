from flask import Blueprint, request, jsonify
from app.models.ai_model import ai_model

# Tạo Blueprint cho review
review_bp = Blueprint('review', __name__)

@review_bp.route('/predict', methods=['POST'])
def predict_review():
    try:
        # 1. Lấy dữ liệu từ Frontend gửi lên
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Vui lòng cung cấp nội dung review (field "text")'}), 400
        
        review_text = data['text']

        # 2. Gọi AI Model để dự đoán
        label, confidence = ai_model.predict(review_text)

        if label is None:
            return jsonify({'error': 'Mô hình AI chưa sẵn sàng'}), 500

        # 3. Trả kết quả về cho Frontend
        # Mapping nhãn cho dễ hiểu (Tùy thuộc vào dữ liệu train của bạn là 'CG'/'OR' hay '1'/'0')
        # Giả sử model trả về 'CG' (Computer Generated) hoặc 'OR' (Original)
        
        result = {
            'text': review_text,
            'label': label,       # 'CG' hoặc 'OR'
            'confidence': confidence
        }
        
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500