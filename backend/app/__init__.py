from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Cấu hình CORS: Cho phép mọi nguồn (hoặc chỉ định rõ http://localhost:3000)
    CORS(app) 
    
    # Đăng ký các Controller (Blueprint)
    from app.controllers.review_controller import review_bp
    app.register_blueprint(review_bp)
    
    # Route kiểm tra server sống hay chết
    @app.route('/', methods=['GET'])
    def health_check():
        return "Server AI đang hoạt động!", 200
        
    return app