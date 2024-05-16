import fitz  # PyMuPDF
from openai import OpenAI
import os

# APIキーを直接指定
api_key = 'openAIkey'

# OpenAIクライアントを設定
client = OpenAI(api_key=api_key)

# PDFを読み込む関数
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# 翻訳する関数
def translate_text(text, target_language="en"):
    response = client.completions.create(
        model="gpt-4o",  # GPT-3.5 Turbo Instructモデルを使用
        prompt=f"Translate the following text to {target_language}:\n\n{text}",
        max_tokens=2000,
        temperature=0.3
    )
    translated_text = response.choices[0].text.strip()
    return translated_text

# LaTeXコードに変換する関数
def text_to_latex(text):
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",  # GPT-3.5 Turbo Instructモデルを使用
        prompt=f"Convert the following text to LaTeX code:\n\n{text}",
        max_tokens=2000,
        temperature=0.3
    )
    latex_code = response.choices[0].text.strip()
    return latex_code

# 全工程を実行する関数
def pdf_to_latex(file_path, target_language="en"):
    # PDFを読み込む
    original_text = read_pdf(file_path)
    
    # テキストを翻訳する
    translated_text = translate_text(original_text, target_language)
    
    # LaTeXコードに変換する
    latex_code = text_to_latex(translated_text)
    
    return latex_code

# ファイルパスを指定して実行
file_path = r"C:\Users\gamiy\note\resource.pdf"  # ここにPDFファイルのパスを指定
latex_code = pdf_to_latex(file_path)
print(latex_code)
