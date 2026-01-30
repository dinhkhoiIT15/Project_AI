import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Khởi tạo các công cụ xử lý ngôn ngữ
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def text_process(review):
    """
    Hàm xử lý văn bản tùy chỉnh để dùng trong CountVectorizer (analyzer).
    Thực hiện:
    1. Xóa dấu câu.
    2. Tách từ & xóa stopwords.
    3. Stemming & Lemmatization.
    Trả về: List các token (từ) đã làm sạch.
    """
    if not isinstance(review, str):
        return []

    # 1. Loại bỏ dấu câu
    nopunc = [char for char in review if char not in string.punctuation]
    nopunc = ''.join(nopunc)

    # 2. Tách từ và loại bỏ stopwords
    clean_tokens = [word for word in nopunc.split() if word.lower() not in stop_words]

    # 3. Stemming và Lemmatization (Kết hợp cả hai như dự án mẫu Part 1)
    final_tokens = []
    for word in clean_tokens:
        stemmed = stemmer.stem(word)       # Ví dụ: running -> run
        lemmatized = lemmatizer.lemmatize(stemmed) # Đưa về dạng chuẩn
        final_tokens.append(lemmatized)

    return final_tokens