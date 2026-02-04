from app import create_app, db
from app.models.user import Admin

# Khởi tạo ứng dụng để lấy context Database
app = create_app()

def seed_admin():
    with app.app_context():
        # 1. Kiểm tra xem Admin đã tồn tại chưa
        existing_admin = Admin.query.filter_by(username='admin').first()
        
        if existing_admin:
            print("⚠️ Tài khoản Admin đã tồn tại! Không cần tạo lại.")
            return

        # 2. Tạo Admin mới
        # Lưu ý: Không cần truyền tham số 'role' vì Class Admin đã tự định nghĩa nó là 'admin'
        admin = Admin(
            username='admin',
            email='admin@system.com',
            phone_number='0999999999',
            account_status='active'
        )
        
        # 3. Mã hóa mật khẩu
        admin.set_password('admin123')

        # 4. Lưu vào Database
        try:
            db.session.add(admin)
            db.session.commit()
            print("✅ Đã tạo tài khoản Admin thành công!")
            print("👉 Username: admin")
            print("👉 Password: admin123")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Lỗi khi tạo Admin: {e}")

if __name__ == "__main__":
    seed_admin()