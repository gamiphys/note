import os
from PyPDF2 import PdfMerger

# ファイルAのディレクトリを取得する
script_directory = os.path.dirname(__file__)

# 結合するフォルダのリストを初期化する
folder_paths = []

# ユーザが "end" と入力するまでフォルダ名を受け付ける
while True:
    folder_name = input("Enter the folder name to merge (or 'end' to stop): ").strip()
    if folder_name.lower() == "end":
        break
    folder_path = os.path.join(script_directory, folder_name)
    if os.path.exists(folder_path):
        folder_paths.append(folder_path)
    else:
        print(f"Error: Folder '{folder_name}' does not exist.")

# 結合するPDFファイルのリストを初期化する
pdf_files = []

# 各フォルダ内のPDFファイルを取得する
for folder_path in folder_paths:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))

# 取得したPDFファイルを結合する
pdf_file_merger = PdfMerger()
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as f:
        pdf_file_merger.append(f)

# 結合後のファイル名を入力
output_file_name = input("Enter the output PDF file name: ")

# 結合したファイルを保存
output_file_path = os.path.join(script_directory, output_file_name)
with open(output_file_path, 'wb') as f:
    pdf_file_merger.write(f)