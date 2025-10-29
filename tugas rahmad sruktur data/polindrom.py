def is_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    # Compare string with its reverse
    return text == text[::-1]

# Test the function
while True:
    user_input = input("Masukkan kata/kalimat (atau ketik 'keluar' untuk berhenti): ")
    
    if user_input.lower() == 'keluar':
        break
        
    if is_palindrome(user_input):
        print(f"'{user_input}' adalah palindrom")
    else:
        print(f"'{user_input}' bukan palindrom")