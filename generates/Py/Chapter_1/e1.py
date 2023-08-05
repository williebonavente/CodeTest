def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_val = ord(char)
            encrypted_ascii_val = (ascii_val - ord('a') + shift) % 26 + ord('a')
            result += chr(encrypted_ascii_val)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    # Get the shopping list from the user and encrypt it
    items = input("Enter the items in your shopping list (separated by commas): ")
    encrypted_items = caesar_cipher_encrypt(items.lower(), 3)  # Encrypt using Caesar Cipher with shift of 3
    shopping_list = encrypted_items.split(',')

    # Get the item to search for and encrypt it
    target_item = input("Enter the item you want to find: ")
    encrypted_target_item = caesar_cipher_encrypt(target_item.lower(), 3)  # Encrypt using Caesar Cipher with shift of 3

    # Perform linear search to check if the item is in the list
    index = linear_search(shopping_list, encrypted_target_item)

    # Display the result
    if index != -1:
        decrypted_target_item = caesar_cipher_decrypt(shopping_list[index], 3)  # Decrypt the found item
        print(f"{decrypted_target_item.capitalize()} is found in the shopping list at index {index}.")
    else:
        decrypted_target_item = caesar_cipher_decrypt(encrypted_target_item, 3)  # Decrypt the target item
        print(f"{decrypted_target_item.capitalize()} is not found in the shopping list.")

if __name__ == "__main__":
    main()
