class Node {
  constructor(value, x, y) {
    this.value = value
    this.neighbors = new Set()
    this.x = x
    this.y = y
  }

  connectNode(neighborNode) {
    this.neighbors.add(neighborNode)
    neighborNode.neighbors.add(this)
  }

  disconnectNode(nodeToDisconnect) {
    this.neighbors.delete(nodeToDisconnect)
    nodeToDisconnect.neighbors.delete(this)
  }

  getData() {
    let info = `Nodo ${this.value} Vecinos: `

    for(let i of this.neighbors) {
      info += `${i.value} `
    }

    return info
  }

  getCoords() {
    return `Nodo ${this.value} x: ${this.x} y: ${this.y}`
  }
}

function generateBoard(height, width) {
  const board = Array(height).fill().map(() => Array(width).fill(null))
  let cellIndex = 1

  for(let i = 0; i < height; i++) {

    for(let j = 0; j < width; j++) {
  
      board[i][j] = new Node(`${cellIndex}B`, i, j)
      cellIndex++
  
    }
  }

  return board
}

// console.log(generateBoard(5,5))

function generateBoardNeighbors(board, height, width) {
  for(let i = 0; i < height; i++) {

    for(let j = 0; j < width; j++) {

      // Conectar vecino izquierdo si es que existe
      if(board[i][j - 1]) {
        board[i][j].connectNode(board[i][j - 1])
      }

      // Conectar vecino derecho si es que existe
      if(board[i][j + 1]) {
        board[i][j].connectNode(board[i][j + 1])
      }

      // Conectar vecino superior si es que existe
      if(board[i - 1]) {
        board[i][j].connectNode(board[i - 1][j])
      }

      // Conectar vecino inferior si es que existe
      if(board[i + 1]) {
        board[i][j].connectNode(board[i + 1][j])
      }
    }
  }

  return board
}

const finalBoard = generateBoardNeighbors(generateBoard(5,5),5,5)

finalBoard[1][2].value = 'Rojo'
finalBoard[0][2].disconnectNode(finalBoard[1][2])

for(let i = 0; i < 5; i++) {
  for(let j = 0; j < 5; j++) {
    console.log(finalBoard[i][j].getData())
  }
}