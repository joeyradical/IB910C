""" The Move class is used to represent a move (either player or computer). It features an 'id' (the chosen move),
coordinates (a tuple which says where on the screen the move icon is supposed to be drawn), an icon, start_coordinates
(the initial coordinates of a move), and a boolean variable which says whether the move is selected or not)
"""


class Move:
	def __init__(self, icon, m_id, coords, clicked):
		self.icon = icon
		self.m_id = m_id
		self.coords = coords
		self.start_coords = coords
		self.clicked = clicked
		
	def set_coords(self, new_coords):
		self.coords = new_coords
	
	def get_start_coords(self):
		return self.start_coords

	def get_id(self):
		return self.m_id
		
	def get_coords(self):
		return self.coords
		
	def get_icon(self):
		return self.icon

	def set_icon(self, icon):
		self.icon = icon
	
	def set_id(self, m_id):
		self.m_id = m_id
		
	def set_clicked(self, state):
		self.clicked = state
		
	def is_clicked(self):
		if self.clicked:
			return True
		else:
			return False
