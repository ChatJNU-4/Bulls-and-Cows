game_start = False

if(str(input("숫자야구를 시작하려면 start를 입력해주세요: ")) == "start"):
	game_start = True
	print("숫자야구를 시작합니다")

while (game_start == True):
	try_num = 0	

	random_numbers = []
	input_numbers = []

	bulls_count = 4
	cows_count = 0

	while (bulls_count < 4):
		print(random_numbers, input_numbers)
		print("bulls: ", bulls_count, ", cows: ", cows_count)

	if (bulls_count == 4):
		print("축하합니다! 정답입니다!")
		print(try_num, "번만에 맞혔습니다")
		game_start = False
