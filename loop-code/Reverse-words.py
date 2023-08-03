str="This is harikrishna palakila"
words = str.split(" ")
print(words)

reverse_word = words[-1::-1]
print(reverse_word)

required_word = ' '.join(reverse_word)

print(required_word)
