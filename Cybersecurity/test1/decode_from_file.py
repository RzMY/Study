import base64

def decode_base64_to_pdf(input_txt_file):
    with open(input_txt_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # 按逗号分隔文件名和 Base64 内容
        parts = line.split(',', 1)
        if len(parts) != 2:
            print(f"跳过无效行: {line}")
            continue
        
        encoded_file_name, base64_content = parts
        
        file_name = base64.b64decode(encoded_file_name).decode('gbk')
        output_file = file_name
        
        # 解码 Base64 并写入 PDF 文件
        pdf_data = base64.b64decode(base64_content)
        with open(output_file, 'wb') as pdf_file:
            pdf_file.write(pdf_data)
        print(f"成功生成文件: {output_file}")

decode_base64_to_pdf('240423200425990_51fangjiatongzhi.pdf.base64.txt')