from PIL import Image
import argparse

# 首先，构建命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

arg = parser.parse_args()
Img = arg.file
width = arg.width
height = arg.height
output = arg.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gry = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gry / unit)]


if __name__ == '__main__':
    im = Image.open(Img)
    im = im.resize((width, height), Image.NEAREST)
    txt = ''
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)


    if output:
        with open(output,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
