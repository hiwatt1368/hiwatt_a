import math

def calculate_tf(word, document):
  """
  محاسبه فرکانس ترم (TF) برای یک کلمه در یک سند.

  Args:
    word: کلمه ای که می خواهیم TF آن را محاسبه کنیم.
    document: سندی که می خواهیم TF را در آن محاسبه کنیم.

  Returns:
    TF word در document.
  """
  return document.count(word) / len(document)

def calculate_idf(word, corpus):
  """
  محاسبه فرکانس معکوس سند (IDF) برای یک کلمه در یک مجموعه اسناد.

  Args:
    word: کلمه ای که می خواهیم IDF آن را محاسبه کنیم.
    corpus: مجموعه اسناد مورد بررسی.

  Returns:
    IDF word در corpus.
  """
  document_count = 0
  for document in corpus:
    if word in document:
      document_count += 1
  return math.log10(len(corpus) / document_count)

def calculate_tfidf(word, document, corpus):
  """
  محاسبه TF-IDF برای یک کلمه در یک سند.

  Args:
    word: کلمه ای که می خواهیم TF-IDF آن را محاسبه کنیم.
    document: سندی که می خواهیم TF-IDF را در آن محاسبه کنیم.
    corpus: مجموعه اسناد مورد بررسی.

  Returns:
    TF-IDF word در document.
  """
  tf = calculate_tf(word, document)
  idf = calculate_idf(word, corpus)
  return tf * idf

# نمونه ای از مجموعه اسناد
corpus = [
    "این یک سند نمونه است که در مورد یادگیری ماشین صحبت می کند.",
    "این سند دیگر در مورد یادگیری عمیق است.",
    "سند سوم در مورد پردازش زبان طبیعی است."
]

# پیش پردازش اسناد (اختیاری)
# می توانید از stemming یا lemmatization برای عادی سازی کلمات قبل از محاسبه TF-IDF استفاده کنید.

# محاسبه TF-IDF برای هر کلمه در هر سند
tfidf_matrix = []
for document in corpus:
  row = []
  for word in document.split():
    row.append(calculate_tfidf(word, document, corpus))
  tfidf_matrix.append(row)

# چاپ ماتریس TF-IDF
print("------ ماتریس TF-IDF ------")
for row in tfidf_matrix:
  print(row)
