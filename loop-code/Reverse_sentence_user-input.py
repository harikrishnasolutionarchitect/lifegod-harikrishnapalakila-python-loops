sentence=input("Enter any sentence: ")
split_sentence=sentence.split(" ")
print(split_sentence)

reverse_sentence=split_sentence[-1::-1]
print(reverse_sentence)

final_sentence=" ".join(reverse_sentence)
print(final_sentence)