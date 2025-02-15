class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.neighbors = set()
        self.x = x
        self.y = y

    def connect_node(self, neighbor_node):
        self.neighbors.add(neighbor_node)
        neighbor_node.neighbors.add(self)

    def disconnect_node(self, node_to_disconnect):
        self.neighbors.discard(node_to_disconnect)
        node_to_disconnect.neighbors.discard(self)

    def get_data(self):
        info = f"Nodo {self.value} Vecinos: "
        info += " ".join([neighbor.value for neighbor in self.neighbors])
        info += f" Coordenadas: x: {self.x} y: {self.y}"
        return info

def generate_board(height, width):
    board = [[None for _ in range(width)] for _ in range(height)]
    cell_index = 1

    for i in range(height):
        for j in range(width):
            board[i][j] = Node(f"{cell_index}B", i, j)
            cell_index += 1

    return board

def generate_board_neighbors(board, height, width):
    for i in range(height):
        for j in range(width):
            # Conectar vecino izquierdo si existe
            if j > 0:
                board[i][j].connect_node(board[i][j - 1])
            # Conectar vecino derecho si existe
            if j < width - 1:
                board[i][j].connect_node(board[i][j + 1])
            # Conectar vecino superior si existe
            if i > 0:
                board[i][j].connect_node(board[i - 1][j])
            # Conectar vecino inferior si existe
            if i < height - 1:
                board[i][j].connect_node(board[i + 1][j])
    
    return board

# Crear y conectar el tablero
board = generate_board(5, 5)
board = generate_board_neighbors(board,5, 5)

# Asignar nombres a los nodos correspondientes
board[1][0].value = '6Museo'
board[1][2].value = '8Drugstore'
board[1][4].value = '10Bankery'
board[3][0].value = '16Libary'
board[3][2].value = '18CityHall'
board[3][4].value = '20School'

#desconectar nodos con paredes 
board[0][0].disconnect_node(board[1][0])
board[1][2].disconnect_node(board[1][1])
board[1][2].disconnect_node(board[1][3])
board[1][4].disconnect_node(board[2][4])
board[3][0].disconnect_node(board[2][0])
board[3][2].disconnect_node(board[2][2])
board[3][2].disconnect_node(board[4][2])
board[3][4].disconnect_node(board[4][4])

# Imprimir la información de los nodos
for i in range(5):
    for j in range(5):
        print(board[i][j].get_data())