import os
from PIL import Image, ImageOps

def process_images(input_image_path, template_path, output_path):
    """
    处理图像并合成最终效果的函数

    参数:
    input_image_path (str): 输入大图的路径
    template_path (str): 模板图片路径
    output_path (str): 输出图片的保存路径
    """
    # 处理原始图片
    with Image.open(input_image_path) as img:
        img = ImageOps.exif_transpose(img)
        # 转换为RGBA模式以支持透明度
        img = img.convert("RGBA")
        # 等比例裁剪缩放至68x68
        resized_img = ImageOps.fit(img, (68, 68), method=Image.LANCZOS, centering=(0.5, 0.5))
        # 创建77x77透明画布
        canvas = Image.new("RGBA", (77, 77), (0, 0, 0, 0))
        # 计算居中位置（4,4）
        position = ((77 - 68) // 2, (77 - 68) // 2)
        # 将处理后的图片粘贴到画布
        canvas.paste(resized_img, position, resized_img)
    # 处理模板图片
    with Image.open(template_path) as template:
        template = template.convert("RGBA")
        # 将模板叠加到画布
        canvas.paste(template, (0, 0), template)
    # 保存结果
    canvas.save(output_path, "PNG")

if __name__ == "__main__":
    output_names = [
        "advisors_great_engineer.png",
        "advisors_great_scientist.png",
        "advisors_great_prophet.png",
        "advisors_great_merchant.png",
        "advisors_great_writer.png",
        "advisors_great_artist.png",
        "advisors_great_musician.png",
        "advisors_great_admiral.png",
        "advisors_great_general.png",
        "advisors_great_khan.png",
        "advisors_venetian_merchant.png",
        "advisors_commandante_general.png"
    ]
    output_dir = "gfx/interface/se3"
    input_dir = "./.."
    template_path = "./../template.png"
    extensions = ['.png', '.jpg', '.jpeg', '.webp', '.bmp']
    for index in range(len(output_names)):
        found = False
        for ext in extensions:
            input_path = os.path.join(input_dir, f"{index}{ext}")
            if os.path.exists(input_path):
                output_path = os.path.join(output_dir, output_names[index])
                try:
                    process_images(input_path, template_path, output_path)
                    print(f"Success: {index} => {output_names[index]}")
                    found = True
                    break
                except Exception as e:
                    print(f"Error processing {input_path}: {str(e)}")
                    found = True
                    break
        if not found:
            print(f"Warning: No input file found for index {index}")
