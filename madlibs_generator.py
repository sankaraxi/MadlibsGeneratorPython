#opening the story file
with open("story.txt","r") as f:
    story = f.read()


words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

#finding the blank words with enumerate function
for i,char in enumerate(story):

    if char == target_start:
        start_of_word = i

    if char == target_end and target_start != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

#getting input for the missing story from the user
answers ={}

for word in words:
    answer =input("Enter a word for "+word+": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)