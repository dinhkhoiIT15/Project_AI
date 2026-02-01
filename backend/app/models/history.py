from app import db
from datetime import datetime

class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)           # Nội dung review
    label = db.Column(db.String(10), nullable=False)    # Kết quả (CG/OR)
    confidence = db.Column(db.Float, nullable=False)    # Độ tin cậy (%)
    created_at = db.Column(db.DateTime, default=datetime.now) # Thời gian test

    def to_json(self):
        """Chuyển đổi object thành JSON để trả về Frontend"""
        return {
            'id': self.id,
            'text': self.text,
            'label': self.label,
            'confidence': self.confidence,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }