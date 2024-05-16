import os
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def select_files():
    # ファイルダイアログを開いてPDFファイルを選択
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")]
    )
    return list(file_paths)

def save_merged_file(pdf_merger):
    # 保存ファイル名を入力
    output_file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save merged PDF as"
    )
    if output_file_path:
        with open(output_file_path, 'wb') as f:
            pdf_merger.write(f)
        messagebox.showinfo("Success", "PDF files merged successfully!")
    else:
        messagebox.showwarning("Cancelled", "Save operation cancelled.")

def merge_pdfs():
    # PDFファイルを選択
    file_paths = select_files()
    if not file_paths:
        return
    
    pdf_merger = PdfMerger()

    # ファイルを結合
    for file_path in file_paths:
        pdf_merger.append(file_path)
    
    # 結合後のファイルを保存
    save_merged_file(pdf_merger)

# メインウィンドウを作成
root = tk.Tk()
root.title("PDF Merger")
root.geometry("300x150")

# 説明ラベル
label = tk.Label(root, text="Select PDF files to merge:")
label.pack(pady=10)

# 結合ボタン
merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=20)

# メインループを開始
root.mainloop()
