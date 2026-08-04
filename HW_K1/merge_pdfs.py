import os
from PyPDF2 import PdfMerger


def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            print(f"添加文件: {os.path.basename(pdf_file)}")
            merger.append(pdf_file)
        else:
            print(f"警告: 文件不存在 - {pdf_file}")
    
    merger.write(output_path)
    merger.close()
    
    print(f"\n合并完成！输出文件: {output_path}")
    print(f"文件大小: {os.path.getsize(output_path) / 1024:.2f} KB")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    pdf_files = [
        os.path.join(base_dir, "K1_题目1~4", "converter.pdf"),
        os.path.join(base_dir, "K1_题目5~8", "【K1】数值和编码_作业答案.pdf")
    ]
    
    output_path = os.path.join(base_dir, "【K1】数值和编码_answers_v2.pdf")
    
    merge_pdfs(pdf_files, output_path)