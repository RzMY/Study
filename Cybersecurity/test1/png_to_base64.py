import base64

def png_to_base64(png_file_path):
    with open(png_file_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string

def main():
    png_file_path = "sicau.png"
    base64_string = png_to_base64(png_file_path)
    print(f"Base64 Encoded String: {base64_string}")
    
if __name__ == "__main__":
    main()