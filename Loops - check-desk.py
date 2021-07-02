from mc import world
from mc.world import setCuboid, setBlock


def buildCheckDesk(x, y, z):
	"""
	(это многострочный комментарий)
	
	
	основа - cuboid (белые клетки)
	черные клетки строятся по следующему принципу:
	У каждой клетки на доске есть 2 координаты. Для
	удобства будем использовать числовые, начиная с 0.
	Первая клетка имеет координаты (0, 0), последняя -
	(7, 7)
	Если посмотреть на доску, то можно заметить, что 
	координаты черных клеток совпадают по четности. 
	Что это значит. Например, первая клетка с координатами
	(0, 0) будет черной, т.к. первая координата 0 - четное,
	вторая координата 0 - тоже четная. Т.е. четность обеих 
	координат одинакова
	(1, 1) - тоже черная, т.к. обе координаты нечетные.
	
	Задача сводится к тому, чтобы заполнить только те клетки
	доски, чьи координаты совпадают по четности.
	Можно заметить, что если сложить координаты черных клеток,
	то число ВСЕГДА будет четное:
	(2, 4): 2 + 4 = 6 - четное
	(1, 1): 1 + 1 = 2 - четное
	и т.д.
	
	Поэтому условие для построения черной клетки следующее:
		(i + j) % 2
	% - знак остаток от деления. n % 2 - остаток от деления на 2
	Если (n % 2) == 0, число четное. 
	Если (n % 2) == 1, число нечетное. 
	
	
	(конец многострочного комментария)
	"""
	
	setCuboid(x, y, z, x+7, y, z+7, 155)
	for i in range(8):
		for j in range(8):
			if (i + j) % 2  == 0:
				setBlock(i + x, y, j + z, 49)
				
	
buildCheckDesk(5,5,5)