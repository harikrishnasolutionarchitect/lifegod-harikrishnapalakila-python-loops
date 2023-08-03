sentence = "Respect your parents"

sentence = sentence.split(" ")

print(sentence)

reverse_sentence = sentence[-1::-1]
print(reverse_sentence)

final_sentence = ' '.join(reverse_sentence)
print(final_sentence)