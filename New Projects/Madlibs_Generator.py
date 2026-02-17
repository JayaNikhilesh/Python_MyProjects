from idlelib.replace import replace
from multiprocessing.connection import answer_challenge

with open("story.txt","r", encoding='utf-8') as f:
    story = f.read()

words = set()
words = []
start_of_word = -1

target_start = "<"
target_end = ">"

print(story)

for i,char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ":")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)