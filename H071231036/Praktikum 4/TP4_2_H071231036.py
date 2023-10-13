def is_palindrome(word: int) -> int:
    cleaned_word = ''.join(word.split()).lower()
   
    if cleaned_word == cleaned_word[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

input_word = input("Masukkan kata: ")
# result = is_p6alindrome(input_word)
print(is_palindrome(input_word))



