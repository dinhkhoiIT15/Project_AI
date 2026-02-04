from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User, Customer, Admin
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__)

# 1. ĐĂNG KÝ (Register) - Mặc định tạo Customer
@user_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Kiểm tra dữ liệu đầu vào
        required_fields = ['username', 'password', 'email']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Thiếu trường {field}'}), 400

        # Kiểm tra trùng lặp
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email đã tồn tại'}), 400
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': 'Username đã tồn tại'}), 400

        # Tạo đối tượng Customer (Kế thừa từ User)
        new_user = Customer(
            username=data['username'],
            email=data['email'],
            phone_number=data.get('phone_number', ''),
            account_status='active'
        )
        new_user.set_password(data['password']) # Mã hóa password

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Đăng ký thành công!', 'user': new_user.to_json()}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 2. ĐĂNG NHẬP (LogIn)
@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Tìm user trong DB
        user = User.query.filter_by(username=username).first()

        # Kiểm tra mật khẩu và trạng thái khóa
        if user and user.check_password(password):
            if user.account_status == 'locked':
                return jsonify({'error': 'Tài khoản của bạn đã bị khóa!'}), 403
            
            # Tạo Token chứa identity là user_id và role
            # Token này giống như "thẻ ra vào" công ty
            access_token = create_access_token(identity={'id': user.id, 'role': user.role})
            
            return jsonify({
                'message': 'Đăng nhập thành công',
                'token': access_token,
                'user': user.to_json()
            }), 200
        
        return jsonify({'error': 'Sai tên đăng nhập hoặc mật khẩu'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. CẬP NHẬT THÔNG TIN (UpdateInfor)
@user_bp.route('/update', methods=['PUT'])
@jwt_required() # Yêu cầu phải có Token mới được gọi
def update_info():
    try:
        current_user_data = get_jwt_identity() # Lấy thông tin từ Token
        user_id = current_user_data['id']
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User không tồn tại'}), 404

        data = request.get_json()
        
        # Cho phép update phone và email
        if 'phone_number' in data:
            user.phone_number = data['phone_number']
        if 'email' in data:
            # Cần check trùng email nếu đổi email (bỏ qua bước check này cho đơn giản trong MVP)
            user.email = data['email']

        db.session.commit()
        return jsonify({'message': 'Cập nhật thành công', 'user': user.to_json()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500