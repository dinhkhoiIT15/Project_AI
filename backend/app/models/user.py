from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    # --- CÁC THUỘC TÍNH CHUNG (Theo yêu cầu của bạn) ---
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False) # Lưu hash, không lưu password string
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    account_status = db.Column(db.String(20), default='active') # 'active' hoặc 'locked'
    created_at = db.Column(db.DateTime, default=datetime.now)

    # --- CẤU HÌNH KẾ THỪA (POLYMORPHISM) ---
    # Cột này dùng để phân biệt đây là Admin hay Customer
    role = db.Column(db.String(20), nullable=False) 

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    # --- CÁC METHODS CHUNG ---
    def set_password(self, password):
        """Mã hóa mật khẩu"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Kiểm tra mật khẩu"""
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            'user_id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone_number,
            'role': self.role,
            'status': self.account_status
        }

# --- CLASS CON: ADMIN ---
class Admin(User):
    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }
    
    # Admin có thể có method riêng nếu cần sau này
    def lock_customer(self, customer):
        if isinstance(customer, Customer):
            customer.account_status = 'locked'
            return True
        return False

# --- CLASS CON: CUSTOMER ---
class Customer(User):
    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }
