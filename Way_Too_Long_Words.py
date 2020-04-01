user_input_count = input()
raw_input_word = []
result_words = []


def shorten_input(word):
    word_length = len(word)
    if word_length > 10:
        return word[0] + str((word_length - 2)) + word[word_length - 1]
    else:
        return word


for i in range(0, int(user_input_count)):
    word = input()
    result_words.append(shorten_input(word))

for i in range(0, len(result_words)):
    print(result_words[i])
