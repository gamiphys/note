from PyPDF2 import PdfMerger

pdf_file_merger = PdfMerger()

# 結合するファイル名のリストを作成
file_names = []
while True:
    file_name = input("Enter the PDF file name to merge (or 'end' to stop): ")
    if file_name.lower() == "end":
        break
    file_names.append(file_name)

# ファイルを結合
for file_name in file_names:
    with open(file_name, 'rb') as f:
        pdf_file_merger.append(f)

# 結合後のファイル名を入力
output_file_name = input("Enter the output PDF file name: ")

# 結合したファイルを保存
with open(output_file_name, 'wb') as f:
    pdf_file_merger.write(f)