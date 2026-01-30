import pandas as pd
import joblib
import os
import sys

# Thiết lập đường dẫn để import được module từ app.utils
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, '..')
sys.path.append(backend_dir)

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Import hàm xử lý văn bản từ cấu trúc MVC
from app.utils.text_processing import text_process

# Đường dẫn file
DATA_PATH = os.path.join(backend_dir, '..', 'data', 'fake_reviews_dataset.csv')
MODEL_PATH = os.path.join(backend_dir, 'ml_artifacts', 'svc_fake_reviews_model.pkl')

def train():
    print("=== BẮT ĐẦU HUẤN LUYỆN MÔ HÌNH SVC ===")
    
    # 1. Tải dữ liệu
    print(f"1. Đang đọc dữ liệu từ: {DATA_PATH}")
    if not os.path.exists(DATA_PATH):
        print("LỖI: Không tìm thấy file dữ liệu CSV.")
        return

    df = pd.read_csv(DATA_PATH)
    df = df.head(100) # Lấy 100 để test
    
    # Chuẩn hóa tên cột (dữ liệu mẫu có thể là 'text_', dữ liệu của bạn là 'text')
    if 'text_' in df.columns:
        df.rename(columns={'text_': 'text'}, inplace=True)
    
    # Loại bỏ dữ liệu rỗng
    df.dropna(subset=['text', 'label'], inplace=True)
    
    X = df['text']
    y = df['label']
    
    # Chia tập dữ liệu (70% train, 30% test)
    print("2. Chia tập dữ liệu Train/Test...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    # 3. Xây dựng Pipeline (GIỐNG HỆT DỰ ÁN MẪU)
    print("3. Xây dựng Pipeline (CountVectorizer -> TfidfTransformer -> SVC)...")
    pipeline = Pipeline([
        ('bow', CountVectorizer(analyzer=text_process)),  # Sử dụng hàm xử lý tùy chỉnh
        ('tfidf', TfidfTransformer()),                    # Tính trọng số TF-IDF
        ('classifier', SVC(probability=True))             # Mô hình SVC (probability=True để lấy %)
    ])

    # 4. Huấn luyện
    print("4. Đang huấn luyện (Bước này có thể mất vài phút)...")
    pipeline.fit(X_train, y_train)

    # 5. Đánh giá
    print("5. Đánh giá mô hình...")
    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"   >> Độ chính xác (Accuracy): {accuracy:.4f}")
    print("\n   Báo cáo chi tiết:")
    print(classification_report(y_test, predictions))

    # 6. Lưu mô hình
    print("6. Lưu model vào thư mục ml_artifacts...")
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"   >> Đã lưu thành công: {MODEL_PATH}")

if __name__ == "__main__":
    train()