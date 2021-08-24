alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
alphabet_dictionary = {}
for i in range(len(alphabet_string)):
    alphabet_dictionary[alphabet_string[i]] = -1
user_input_word = input()

for i in range(len(user_input_word)):
    for j in range(len(alphabet_string)):
        if user_input_word[i] == alphabet_string[j] and alphabet_dictionary[user_input_word[i]] == -1:
            alphabet_dictionary[user_input_word[i]] = i

string_to_print = ''

for i in range(len(alphabet_dictionary)):
    string_to_print += str(alphabet_dictionary[alphabet_string[i]]) + ' '
print(string_to_print)
