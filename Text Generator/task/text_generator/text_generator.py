from nltk.tokenize import regexp_tokenize
from nltk.util import trigrams
from collections import Counter
from collections import defaultdict
import random
import regex as re

filename = input()
# for tests
# filename = "corpus.txt"

f = open(filename, "r", encoding="utf-8")
text = ""
for line in f:
    text += line
f.close()

tokens = regexp_tokenize(text, r"\S+")

trigs = list(trigrams(tokens))

dict_head = defaultdict(list)

for trigram in trigs:
    dict_head[trigram[0] + " " + trigram[1]].append(trigram[2])

head_tails = dict()

for head, tails in dict_head.items():
    head_tails[head] = Counter(tails)


num_of_sent = 10
text = ""

def get_first_word():
    while True:
        result = random.choice(list(head_tails.keys()))
        if re.match(r"[A-Z]\w*[^!\.\?] ", result):
            return result

for _ in range(num_of_sent):
    first_word = get_first_word()
    text += first_word
    words_in_sent = 2
    head_ = first_word
    while True:
        tail_ = random.choices(list(head_tails[head_].keys()), list(head_tails[head_].values()))[0]
        text += " " + tail_
        words_in_sent += 1
        if words_in_sent > 4 and re.match(r".+[!\.\?]$", tail_):
            break
        head_ = head_.split(" ")[1] + " " + tail_

    text += "\n"

print(text)
# while True:
#     word = input()
#     if word == "exit":
#         break
#     try:
#         result = head_tails[word].most_common()
#     except KeyError:
#         print("Head:", word)
#         print("The requested word is not in the model. Please input another word.")
#     except (TypeError, ValueError):
#         print("Type Error. Please input an integer.")
#     except IndexError:
#         print("Index Error. Please input an integer that is in the range of the corpus.")
#     else:
#         print("Head:", word)
#         for tail, count in result:
#             print("Tail:", tail, "Count:", count)


# print("Number of bigrams:", len(bigs))

# print("Corpus statistics")
# print("All tokens:", len(tokens))
# print("Unique tokens:", len(set(tokens)))
#
# while True:
#     number = input()
#     if number == "exit":
#         break
#     try:
#         result = tokens[int(number)]
#     except (TypeError, ValueError):
#         print("Type Error. Please input an integer.")
#     except IndexError:
#         print("Index Error. Please input an integer that is in the range of the corpus.")
#     else:
#        print(result)
#
# while True:
#     number = input()
#     if number == "exit":
#         break
#     try:
#         result = bigs[int(number)]
#     except (TypeError, ValueError):
#         print("typerror Type Error. Please input an integer.")
#     except IndexError:
#         print("Index Error. Please input a value that is not greater than the number of all bigrams.")
#     else:
#        print("Head:",result[0], "Tail:", result[1])
