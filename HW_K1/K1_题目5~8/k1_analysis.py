import os
import struct

try:
    from mutagen.mp3 import MP3
    has_mutagen = True
except ImportError:
    has_mutagen = False

try:
    from mido import MidiFile
    has_mido = True
except ImportError:
    has_mido = False

try:
    from PIL import Image
    has_pil = True
except ImportError:
    has_pil = False

try:
    import cv2
    import numpy as np
    has_opencv = True
except ImportError:
    has_opencv = False


def format_size(bytes_size):
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.2f} KB"
    else:
        return f"{bytes_size / (1024 * 1024):.2f} MB"


def format_time(seconds):
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}:{secs:.2f}"


def get_file_size(file_path):
    return os.path.getsize(file_path)


def analyze_mp3(file_path):
    print("=" * 60)
    print("题目5：查阅Test 1 Part 1.mp3文件信息")
    print("=" * 60)
    
    if not has_mutagen:
        print("错误：未安装mutagen库，请运行 pip install mutagen")
        return
    
    audio = MP3(file_path)
    file_size = get_file_size(file_path)
    
    sample_rate = audio.info.sample_rate
    channels = audio.info.channels
    bitrate = audio.info.bitrate / 1000
    duration = audio.info.length
    
    print(f"文件名: {os.path.basename(file_path)}")
    print(f"文件格式: MP3 (MPEG-1 Audio Layer 3)")
    print(f"采样频率: {sample_rate} Hz")
    print(f"声道数: {channels}")
    print(f"码率: {bitrate:.1f} kbps")
    print(f"时长: {format_time(duration)}")
    print(f"文件容量: {format_size(file_size)} ({file_size} 字节)")
    
    original_pcm_size = sample_rate * channels * duration * 16 / 8
    compression_rate = original_pcm_size / file_size
    
    print("\n压缩率计算过程：")
    print(f"原始PCM编码容量 = 采样频率 × 声道数 × 时长 × 位深 / 8")
    print(f"               = {sample_rate} × {channels} × {duration:.2f} × 16 / 8")
    print(f"               = {original_pcm_size:.0f} 字节 ({format_size(original_pcm_size)})")
    print(f"实际文件容量 = {file_size} 字节 ({format_size(file_size)})")
    print(f"压缩率 = 原始容量 / 实际容量 = {compression_rate:.2f}")
    print(f"压缩比 = {100 - (100 / compression_rate):.1f}%")
    print()


def analyze_midi(file_path):
    print("=" * 60)
    print("题目6：查阅圣诞节快乐劳伦斯先生.mid文件信息")
    print("=" * 60)
    
    if not has_mido:
        print("错误：未安装mido库，请运行 pip install mido")
        return
    
    mid = MidiFile(file_path)
    file_size = get_file_size(file_path)
    
    duration = mid.length
    ticks_per_beat = mid.ticks_per_beat
    num_tracks = len(mid.tracks)
    
    print(f"文件名: {os.path.basename(file_path)}")
    print(f"文件格式: MIDI")
    print(f"时长: {format_time(duration)}")
    print(f"文件容量: {format_size(file_size)} ({file_size} 字节)")
    print(f"Ticks per Beat: {ticks_per_beat}")
    print(f"轨道数: {num_tracks}")
    
    total_notes = 0
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0:
                total_notes += 1
    
    print(f"音符总数: {total_notes}")
    print()
    print("收听效果评价：")
    print("MIDI文件不包含实际音频波形数据，而是存储音符事件信息。")
    print("播放时由音源合成声音，音质取决于所使用的音色库。")
    print("该文件为经典钢琴曲《圣诞快乐劳伦斯先生》的MIDI版本，")
    print("旋律清晰优美，但缺乏真实钢琴的丰富音色层次和情感表达。")
    print()


def analyze_image(file_path):
    print("=" * 60)
    print(f"题目7：查阅{os.path.basename(file_path)}文件信息")
    print("=" * 60)
    
    if not has_pil:
        print("错误：未安装Pillow库，请运行 pip install Pillow")
        return
    
    img = Image.open(file_path)
    file_size = get_file_size(file_path)
    
    format_name = img.format
    width, height = img.size
    mode = img.mode
    num_pixels = width * height
    
    if mode == '1':
        color_system = "黑白二值 (1-bit)"
        bits_per_pixel = 1
    elif mode == 'L':
        color_system = "灰度 (8-bit)"
        bits_per_pixel = 8
    elif mode == 'RGB':
        color_system = "RGB真彩色 (24-bit)"
        bits_per_pixel = 24
    elif mode == 'RGBA':
        color_system = "RGBA真彩色带透明通道 (32-bit)"
        bits_per_pixel = 32
    else:
        color_system = mode
        bits_per_pixel = 8
    
    print(f"文件名: {os.path.basename(file_path)}")
    print(f"文件格式: {format_name}")
    print(f"分辨率: {width} × {height}")
    print(f"颜色系统: {color_system}")
    print(f"位深: {bits_per_pixel} bits/pixel")
    print(f"像素总数: {num_pixels}")
    print(f"文件容量: {format_size(file_size)} ({file_size} 字节)")
    
    original_size = num_pixels * bits_per_pixel / 8
    compression_rate = original_size / file_size
    
    print("\n压缩率计算过程：")
    print(f"原始数字图像编码容量 = 像素总数 × 位深 / 8")
    print(f"                     = {num_pixels} × {bits_per_pixel} / 8")
    print(f"                     = {original_size:.0f} 字节 ({format_size(original_size)})")
    print(f"实际文件容量 = {file_size} 字节 ({format_size(file_size)})")
    print(f"压缩率 = 原始容量 / 实际容量 = {compression_rate:.2f}")
    print(f"压缩比 = {100 - (100 / compression_rate):.1f}%")
    
    print("\n5个像素的颜色编码值：")
    sample_positions = [
        (0, 0),
        (width // 4, height // 4),
        (width // 2, height // 2),
        (3 * width // 4, 3 * height // 4),
        (width - 1, height - 1)
    ]
    
    for i, (x, y) in enumerate(sample_positions):
        pixel = img.getpixel((x, y))
        if isinstance(pixel, tuple):
            hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel[:3])
            print(f"  像素{i+1} (位置: {x},{y}): RGB值={pixel}, 十六进制={hex_color}")
        else:
            print(f"  像素{i+1} (位置: {x},{y}): 灰度值={pixel}")
    print()


def analyze_video(file_path):
    print("=" * 60)
    print("题目8：查阅Pascal加法器1645.mp4文件信息")
    print("=" * 60)
    
    if not has_opencv:
        print("错误：未安装opencv-python库，请运行 pip install opencv-python")
        return
    
    cap = cv2.VideoCapture(file_path)
    file_size = get_file_size(file_path)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps if fps > 0 else 0
    
    bitrate_kbps = (file_size * 8) / (duration * 1000) if duration > 0 else 0
    
    print(f"文件名: {os.path.basename(file_path)}")
    print(f"文件格式: MP4 (MPEG-4 Part 14)")
    print(f"分辨率: {width} × {height}")
    print(f"帧率: {fps:.2f} fps")
    print(f"帧数: {frame_count}")
    print(f"时长: {format_time(duration)}")
    print(f"文件容量: {format_size(file_size)} ({file_size} 字节)")
    print(f"码率: {bitrate_kbps:.2f} kbps")
    
    original_size = frame_count * width * height * 24 / 8
    compression_rate = original_size / file_size
    
    print("\n压缩率计算过程：")
    print(f"原始视频编码容量 = 帧数 × 分辨率宽 × 分辨率高 × 位深 / 8")
    print(f"               = {frame_count} × {width} × {height} × 24 / 8")
    print(f"               = {original_size:.0f} 字节 ({format_size(original_size)})")
    print(f"实际文件容量 = {file_size} 字节 ({format_size(file_size)})")
    print(f"压缩率 = 原始容量 / 实际容量 = {compression_rate:.2f}")
    print(f"压缩比 = {100 - (100 / compression_rate):.1f}%")
    print()
    
    cap.release()


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    mp3_path = os.path.join(base_dir, "Test 1 Part 1.mp3")
    midi_path = os.path.join(base_dir, "圣诞节快乐劳伦斯先生.mid")
    image_paths = [
        os.path.join(base_dir, "Lenna1bit.png"),
        os.path.join(base_dir, "lena_gray.png"),
        os.path.join(base_dir, "Lenna.jpg")
    ]
    video_path = os.path.join(base_dir, "Pascal加法器1645.mp4")
    
    print("=" * 60)
    print("【K1】数值和编码 - 作业答案")
    print("=" * 60)
    print()
    
    analyze_mp3(mp3_path)
    analyze_midi(midi_path)
    
    for img_path in image_paths:
        analyze_image(img_path)
    
    analyze_video(video_path)
    
    print("=" * 60)
    print("所有题目分析完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()