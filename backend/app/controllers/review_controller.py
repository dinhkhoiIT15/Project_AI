from flask import Blueprint, request, jsonify
from app.models.ai_model import ai_model
from app.models.history import History  # Import Model
from app import db

review_bp = Blueprint('review', __name__)

# API 1: Dự đoán và Lưu vào DB
@review_bp.route('/predict', methods=['POST'])
def predict_review():
    try:
        # 1. Lấy dữ liệu từ Frontend gửi lên
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Vui lòng cung cấp nội dung review (field "text")'}), 400
        
        review_text = data['text']

        # 2. Gọi AI Model để dự đoán
        # label_raw có thể là numpy.int64 (ví dụ: 1 hoặc 0)
        label_raw, confidence_raw = ai_model.predict(review_text)

        if label_raw is None:
            return jsonify({'error': 'Mô hình AI chưa sẵn sàng'}), 500

        # === PHẦN SỬA LỖI QUAN TRỌNG (FIX INT64 ERROR) ===
        
        # Bước A: Ép kiểu dữ liệu (Numpy -> Python chuẩn) để tránh lỗi JSON
        label_str = str(label_raw)              # Chuyển số 1 thành chuỗi "1"
        confidence_val = float(confidence_raw)  # Chuyển numpy float thành float chuẩn

        # Bước B: Ánh xạ nhãn (Mapping)
        # Nếu model trả về '1' hoặc 'CG' thì là FAKE
        if label_str == '1' or label_str == 'CG':
            final_label = 'CG'  # Computer Generated (Giả)
        else:
            final_label = 'OR'  # Original (Thật)

        # --- LƯU VÀO DATABASE (Code mới thêm) ---
        try:
            new_record = History(
                text=review_text,
                label=final_label,
                confidence=confidence_val
            )
            db.session.add(new_record)
            db.session.commit()
            print("✅ Đã lưu kết quả vào Database!")
        except Exception as db_err:
            db.session.rollback() # Hoàn tác nếu lỗi DB
            print(f"⚠️ Lỗi khi lưu DB: {db_err}")
            # Vẫn trả về kết quả cho user dù lỗi lưu DB

        # 3. Trả kết quả về cho Frontend
        result = {
            'text': review_text,
            'label': final_label,      # Frontend sẽ nhận được 'CG' hoặc 'OR'
            'confidence': confidence_val
        }
        
        return jsonify(result), 200

    except Exception as e:
        # In lỗi ra Terminal để dễ sửa
        print(f"🔥🔥🔥 LỖI BACKEND: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500
    
# API 2: Lấy danh sách lịch sử (Cho tính năng sắp tới)
@review_bp.route('/history', methods=['GET'])
def get_history():
    try:
        # Lấy 10 dòng mới nhất, sắp xếp theo thời gian giảm dần
        records = History.query.order_by(History.created_at.desc()).limit(10).all()
        
        # Chuyển đổi sang JSON
        history_list = [record.to_json() for record in records]
        
        return jsonify(history_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500