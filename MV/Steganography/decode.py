from PIL import Image
import numpy as np

def decode_image(image_path):
    img = np.array(Image.open(image_path))
    img_flat = img.flatten()
    
    decoded_message = ''
    idx = 0
    while True:
        bits = [bin(img_flat[i])[-1] for i in range(idx, idx + 8)]
        bits = ''.join(bits)
        decoded_message += chr(int(bits, 2))
        idx += 8
        if decoded_message[-5:] == '[END]' or idx > img_flat.shape[0] - 8:
            break

    if decoded_message[-5:] != '[END]':
        print("No hidden message")
    else:
        print("Decoded message:", decoded_message)

if __name__ == "__main__":
    image_path = "speechspeechspeech.png"
    decode_image(image_path)
