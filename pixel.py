from PIL import Image
import numpy as np
import os

def encrypt_image(input_image_path, output_image_path):
    # Open the image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Perform pixel manipulation: shift pixel values
    encrypted_array = (img_array + 50) % 256  # Shift pixel values

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Reverse the operation to decrypt
    decrypted_array = (img_array - 50) % 256  # Reverse shift pixel values

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

if __name__ == "__main__":
    # Print the current working directory for troubleshooting
    print("Current Working Directory:", os.getcwd())

    # Update these paths to point to your image files
    input_image_path = r'F:\Prodigy infotech\pixel manipulation\weeknd.jpg'
    encrypted_image_path = r'F:\Prodigy infotech\pixel manipulation\encrypted.jpg'
    decrypted_image_path = r'F:\Prodigy infotech\pixel manipulation\decrypted.jpg'

    # Example usage
    encrypt_image(input_image_path, encrypted_image_path)
    decrypt_image(encrypted_image_path, decrypted_image_path)
