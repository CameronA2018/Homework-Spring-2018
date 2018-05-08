import random

beginning = 1
end = 100
rollRange1 = (beginning,end)
rollRange2 = (beginning,end)
score1 = 0
score2 = 0
ledger = []

bot_nobot = raw_input('Do you want to play the computer or another person? Please respond with "Computer" or "Person" ')

bot = bot_nobot == "Computer"
no_bot = bot_nobot == "Person"

def roll(beginning,end):
	if(bot == True):
		Player_1 = raw_input("What is Player 1's name? ")
		Player1_roll = int(raw_input("Press 1 to Roll "))
		if(Player1_roll == 1):
			return random.randint(beginning,end)
	if(no_bot == True):
		Player_1 = raw_input("What is Player 1's name? ")
		Player_2 = raw_input("What is Player 2's name? ")
		Player1_roll = int(raw_input("Press 1 for "+Player_1+" to Roll "))
		if(Player1_roll == 1):
			return random.randint(beginning,end)
		Player2_roll = int(raw_input("Press 2 for "+Player_2+" to Roll "))
		if(Player2_roll == 2):
			return random.randint(beginning,end)

def findroll_Result1(roll):
	roll_Result1 = roll(beginning,end)*.5
	return roll_Result1

def findroll_Result2(roll):
	roll_Result2 = roll(beginning,end)*.5
	return roll_Result2

def roundWinner(roll_Result1,roll_Result2):
        if(roll_Result1 < roll_Result2):
                return  Player_1 +" Wins the Round"
        elif(roll_Result2 < roll_Result1):
                return Player_2 +" Wins the Round"
        elif(roll_Result1 == 20):
                return Player_2 +" Wins the Round"
        elif(roll_Result2 == 20):
                return Player_1+" Wins the Round"
        else:
                return "Tie and Re-roll"

def gameWinner(score1,score2):
        if(score1 < score2):
                return Player_1 +" Wins the Game"
        elif(score2 < score1):
                return Player_2 +" Wins the Game"
        elif(score1 == score2):
                return "Tie Breaker"
        else:
                return "Somebody Cheated"

gameRunning = 3
while(gameRunning >= 0):
	roll_Result1 = findroll_Result1(roll)
	roll_Result2 = findroll_Result2(roll)
	rollWin = roundWinner(roll_Result1,roll_Result2)
	if(roll_Result1 < roll_Result2):
		score1 += 1
	if(roll_Result2 < roll_Result1):
		score2 += 1
	if(roll_Result1 == 20):
		score2 += 1
	if(roll_Result2 == 20):
		score1 += 1
	gameRunning -= 1
	gameWin = gameWinner(score1,score2)
	if(gameWin != "Tie Breaker"):
		gameRunning += 1
	print(roll_Result1,roll_Result2,rollWin)

print(gameWin)
