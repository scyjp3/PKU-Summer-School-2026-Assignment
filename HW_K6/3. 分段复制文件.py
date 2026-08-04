import os

src_file = 'SourceHanSansSC-Normal.otf'
dst_file = 'copy_of_font.otf'

# 以二进制模式打开源文件
with open(src_file, 'rb') as f_src:
    total_size = f_src.seek(0, 2)
    print("源文件大小：{} 字节（约 {:.2f} MB）".format(total_size, total_size / 1024 / 1024))

    f_src.seek(0)

    # 分段复制：每次读取 chunk_size 字节，写入目标文件
    chunk_size = 1024 
    copied = 0
    with open(dst_file, 'wb') as f_dst:
        while copied < total_size:
            chunk = f_src.read(chunk_size) 
            f_dst.write(chunk)               
            copied += len(chunk)
    print("已复制 {} 字节，复制完成！".format(copied))

print("源文件大小：", os.path.getsize(src_file))
print("目标文件大小：", os.path.getsize(dst_file))
