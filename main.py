import sys

print("Só são válidos números de 1 a 9")
print("Para ganhar os números não devem se repetir nas colunas horizontais ou verticais")
print("Sudokão basico demais, você consegue")

print("")
print("")
print("")

def print_board(x):
	global error
	print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

	for i in range(9):
		print("║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║".format(x[i][0],
			x[i][1],
			x[i][2],
			x[i][3],
			x[i][4],
			x[i][5],
			x[i][6],
			x[i][7],
			x[i][8],))

		if i != 8:
			print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

	if error:
		print("╚═══╧═══╧═══INVÁLIDO!══╧═══╧═══╝")

	else:
		print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")


def check(a):
	lst = []
	for i in range(9):

	
		for j in range(1,10):
			if a[i].count(j) > 1:
				return False

		#checks each column
		for l in range(1,10):
			if lst.count(l) > 1:
				return False
		lst.clear()
		for k in range(9):
			lst.append(a[k][i])

	return True


def get_input():
	global error, x, y
	try:
		
		print(' '*64)
		sys.stdout.write("\033[F")


		inp = input("Digite um número: ")
		if (len(inp) == 1) and (inp != "0"):
			board[x][y] = int(inp)
			error = False
		else:
			raise ValueError
	except:
		error = True


def move_index():
	for i in range(20):
		sys.stdout.write("\033[F")

board = [
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "],
]

error = False


for x in range(9):
	for y in range(9):

		print_board(board)

		get_input()
		
		
		while error:
			move_index()
			print_board(board)
			get_input()

		move_index()


print_board(board)
if check(board):
	print("Acertou o Sudoku!")

elif not(check(board)):
	print("Erroooooooooou!!!")
