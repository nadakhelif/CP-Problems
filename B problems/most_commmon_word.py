import re


paragraph= input() 
banned = input()
banned = banned.split()
# create a dict
d = dict()
clean_paragraph = re.sub(r'[^\w\s]', ' ', paragraph)
l = clean_paragraph.lower().split()
for i in l:
    word = ''.join(char for char in i if char.isalnum())
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
most_common_word = ""
highest_count = 0

for word, count in d.items():
    # Ensure the word is not in the banned list
    if word not in banned and count > highest_count:
        most_common_word = word
        highest_count = count

# Return the most common word that is not banned
print(most_common_word) 
        




