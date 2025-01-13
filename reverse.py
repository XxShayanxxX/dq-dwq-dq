def reverse_words(text):
    return ' '.join(text.split()[::-1])

# Example Usage:
text = "Hello world, how are you?"
print(reverse_words(text))
