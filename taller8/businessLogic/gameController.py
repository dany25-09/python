from itertools import cycle
from data.move import Move


class GameController:
    def __init__(self, players, boardSize):
        self._players = cycle(players)
        self._boardSize = boardSize
        self._currentPlayer = next(self._players)
        self._winnerCombo = []
        self._currentMoves = []
        self._hasWinner = False
        self._winningCombos = []
        self._setupMoves()

    def _setupMoves(self):
        self._currentMoves = [
            [Move(row, col, '') for col in range(self._boardSize)]
            for row in range(self._boardSize)
        ]
        self._winningCombos = self._getWinningCombos()

    def _getWinningCombos(self):
        rows = [
            [(move.getRow(), move.getCol()) for move in row]
            for row in self._currentMoves
        ]
        columns = [list(col) for col in zip(*rows)]
        firstDiagonal = [row[i] for i, row in enumerate(rows)]
        secondDiagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [firstDiagonal, secondDiagonal]

    def isValidMove(self, move):
        """Return True if move is valid, and False otherwise."""
        row, col = move.getRow(), move.getCol()
        move_was_not_played = self._currentMoves[row][col].getSymbol() == ""
        return not self._hasWinner and move_was_not_played

    def processMove(self, move):
        """Process the current move and check if it's a win."""
        row, col = move.getRow(), move.getCol()
        self._currentMoves[row][col] = move
        for combo in self._winningCombos:
            results = set(
                self._currentMoves[n][m].getSymbol()
                for n, m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._hasWinner = True
                self._winnerCombo = combo
                break

    def hasWinner(self):
        """Return True if the game has a winner, and False otherwise."""
        return self._hasWinner

    def isTied(self):
        """Return True if the game is tied, and False otherwise."""
        played_moves = (
            move.getSymbol() for row in self._currentMoves for move in row
        )
        return not self._hasWinner and all(played_moves)

    def togglePlayer(self):
        """Return a toggled player."""
        self._currentPlayer = next(self._players)

    def resetGame(self):
        """Reset the game state to play again."""
        self._setupMoves()
        self._hasWinner = False
        self._winnerCombo = []

    def getCurrentPlayer(self):
        return self._currentPlayer

    def getBoardSize(self):
        return self._boardSize

    def getWinnerCombo(self):
        return self._winnerCombo