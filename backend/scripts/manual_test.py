import joblib
import os
import sys
import pandas as pd

# 1. Thiết lập đường dẫn (để import được app.utils)
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, '..')
sys.path.append(backend_dir)

# 2. Import đường dẫn file model
MODEL_PATH = os.path.join(backend_dir, 'ml_artifacts', 'svc_fake_reviews_model.pkl')

def test_ai():
    # Kiểm tra xem có file model chưa
    if not os.path.exists(MODEL_PATH):
        print(f"Lỗi: Không tìm thấy model tại {MODEL_PATH}")
        print("Hãy chạy 'python scripts/train_model.py' trước!")
        return

    print("--- ĐANG TẢI MÔ HÌNH AI... ---")
    try:
        # Load model đã lưu
        model = joblib.load(MODEL_PATH)
        print(">> Tải model thành công!")
    except Exception as e:
        print(f"Lỗi khi load model: {e}")
        return

    # 3. Danh sách các câu Review mẫu để test
    # Bạn có thể tự thêm câu của mình vào đây
    test_reviews = [
        "I love this product! It works exactly as described and arrived on time.",  # Câu có vẻ Thật (OR)
        "The item is terrible. Do not buy it. Waste of money.",                   # Câu có vẻ Thật (OR)
        "As an AI language model, I cannot write a review for this product.",      # Câu Giả (CG) rõ ràng
        "Excellent quality, fast shipping, highly recommended.",                   # Câu chung chung
    ]

    print("\n--- KẾT QUẢ DỰ ĐOÁN ---")
    print(f"{'REVIEW TEXT':<60} | {'DỰ ĐOÁN':<10} | {'ĐỘ TIN CẬY':<10}")
    print("-" * 90)

    # Dự đoán cho từng câu
    predictions = model.predict(test_reviews)
    probs = model.predict_proba(test_reviews) # Lấy xác suất

    for i, text in enumerate(test_reviews):
        label = predictions[i]
        confidence = max(probs[i]) * 100 # Lấy % cao nhất
        
        # Cắt ngắn text để hiển thị cho đẹp
        display_text = (text[:57] + '...') if len(text) > 57 else text
        
        print(f"{display_text:<60} | {label:<10} | {confidence:.2f}%")

if __name__ == "__main__":
    test_ai()