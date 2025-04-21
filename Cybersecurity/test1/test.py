import base64

encoded_str = "udjT2jIwMjTE6qGwzuXSu6Gxt8W82bXEzajWqi5wZGY="
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('gbk')
print(decoded_str)