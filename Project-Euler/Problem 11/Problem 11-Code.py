grid = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
grid = grid.split(' ')

def return_r(i):
	return grid[i:i+20]

r_1 = return_r(0)
r_2 = return_r(20)
r_3 = return_r(40)
r_4 = return_r(60)
r_5 = return_r(80)
r_6 = return_r(100)
r_7 = return_r(120)
r_8 = return_r(140)
r_9 = return_r(160)
r_10 = return_r(180)
r_11 = return_r(200)
r_12 = return_r(220)
r_13 = return_r(240)
r_14 = return_r(260)
r_15 = return_r(280)
r_16 = return_r(300)
r_17 = return_r(320)
r_18 = return_r(340)
r_19 = return_r(360)
r_20 = return_r(380)

grid = (r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8, r_9, r_10, r_11, r_12, r_13, r_14, r_15, r_16, r_17, r_18, r_19, r_20)

for i in range(20):
	for j in range(20):
		if grid[i][j].startswith('0'):
			grid[i][j] = grid[i][j][1]

		grid[i][j] = int(grid[i][j])

current_max = 0

for i in range(20):
	for j in range(20):
		try:
			hor = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
			if hor > current_max:
				current_max = hor
		except IndexError:
			pass

		try:
			vert = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
			if vert > current_max:
				current_max = vert
		except IndexError:
			pass		

		try:
			dgr = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
			if dgr > current_max:
				current_max = dgr
		except IndexError:
			pass

		try:
			dgl = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
			if dgl > current_max:
				current_max = dgl
		except IndexError:
			pass

print(current_max)
