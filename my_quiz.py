import json, time, math

with open("my_quiz.json") as quiz_file:
	quiz = json.load(quiz_file)

username = input("Please enter your name: ")
print("Lets begin!\n")

score = 0

for question in quiz:
	print(quiz[question]["question"])
	answer = input("Please give your answer: ")
	if answer == quiz[question]["answer"]:
		time.sleep(1)
		print("That is correct!\n")
		score += 1
		time.sleep(1)
	else:
		time.sleep(1)
		print(f'I\'m afraid that\'s incorrect. The correct answer is {quiz[question]["answer"]}\n')
		time.sleep(1)

if score >= 8:
	print(f"Well done! You scored {score} out of 10")
elif score >= 5:
	print(f"Not bad. You scored {score} out of 10")
else:
	print(f"Oh dear. You scored {score} out of 10")

final_score = str(score)

quiz_scores = open("quiz_scores.txt", "a")
quiz_scores.write(str(username + ": " + final_score + "\n"))
quiz_scores.close()

quiz_scores = open("quiz_scores.txt", "r")
lines = quiz_scores.readlines()
quiz_scores.close()

totalScore = 0
for line in lines:
	totalScore += int(line.rstrip().split(": ")[1])

average = (totalScore/len(lines))
print(f"The average score for this quiz is: {average}")