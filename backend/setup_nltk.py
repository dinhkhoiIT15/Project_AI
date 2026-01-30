import nltk

print("Đang tải các gói dữ liệu NLTK cần thiết...")

# Tải danh sách từ dừng (stopwords)
nltk.download('stopwords')

# Tải dữ liệu từ điển cho Lemmatization
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt') # Cần thiết cho tokenization

print("Đã tải xong!")