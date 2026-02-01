from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# 1. Khởi tạo object Database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Cấu hình CORS: Cho phép mọi nguồn (hoặc chỉ định rõ http://localhost:3000)
    CORS(app) 

    # 2. Cấu hình kết nối Database PostgreSQL
    # Cú pháp: postgresql://username:password@localhost:5432/database_name
    # HÃY SỬA MẬT KHẨU CỦA BẠN Ở DƯỚI (chỗ YOUR_PASSWORD)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/project_ai'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 3. Kết nối DB với App
    db.init_app(app)
    
    # 4. Đăng ký các Controller (Blueprint)
    from app.controllers.review_controller import review_bp
    app.register_blueprint(review_bp)

    # 5. Tự động tạo bảng nếu chưa có
    with app.app_context():
        # Import model để SQLAlchemy biết cấu trúc bảng
        from app.models.history import History 
        db.create_all()  # Lệnh này sẽ tạo bảng 'history' trong PostgreSQL ngay lập tức
        print("✅ Đã kết nối Database và kiểm tra bảng thành công!")
    
    # Route kiểm tra server sống hay chết
    @app.route('/', methods=['GET'])
    def health_check():
        return "Server AI đang hoạt động!", 200
        
    return app