import tkinter as tk
from tkinter import font
from data.move import Move


class TicTacToeBoard(tk.Tk):
    def __init__(self, gameController):
        super().__init__()
        self.title("Triqui")
        self._cells = {}
        self._gameController = gameController
        self.configure(background = "yellow")
        self._createMenu()
        self._createBoardDisplay()
        self._createBoardGrid()

    def _createBoardDisplay(self):
        displayFrame = tk.Frame(master=self,background = "DarkOrchid1")
        displayFrame.pack(fill=tk.X)
        self.display = tk.Label(
            background = "DarkOrchid1",
            master=displayFrame,
            text="¿Empezamos?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _createBoardGrid(self):
        gridFrame = tk.Frame(master=self, background = "yellow")
        gridFrame.pack()
        for row in range(self._gameController.getBoardSize()):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._gameController.getBoardSize()):
                button = tk.Button(
                    relief = tk.RIDGE,
                    borderwidth = 20,
                    background = "DarkOrchid1",
                    master=gridFrame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.cellClicked)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

    def cellClicked(self, event):
        """Handle a player's move."""
        clickedBtn = event.widget
        row, col = self._cells[clickedBtn]
        playerSymbol = self._gameController.getCurrentPlayer().getSymbol()
        playerColor = self._gameController.getCurrentPlayer().getColor()
        move = Move(row, col, playerSymbol)
        if self._gameController.isValidMove(move):
            self._updateButton(clickedBtn, playerSymbol, playerColor)
            self._gameController.processMove(move)
            if self._gameController.isTied():
                self._updateDisplay(msg="Empate!", color="red")
            elif self._gameController.hasWinner():
                self._highlightCells()
                msg = f'Jugador "{playerSymbol}" ganó!'
                self._updateDisplay(msg, playerColor)
            else:
                self._gameController.togglePlayer()
                msg = f'Turno para "{self._gameController.getCurrentPlayer().getSymbol()}'
                self._updateDisplay(msg)

    def _updateButton(self, clickedBtn, playerSymbol, playerColor):
        clickedBtn.config(text=playerSymbol)
        clickedBtn.config(fg=playerColor)

    def _updateDisplay(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlightCells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._gameController.getWinnerCombo():
                button.config(highlightbackground="red")

    def _createMenu(self):
        menuBar = tk.Menu(master=self)
        self.config(menu=menuBar)
        playMenu = tk.Menu(master=menuBar)
        playMenu.add_command(
            label="Reiniciar juego",
            command=self.resetBoard
        )
        playMenu.add_separator()
        playMenu.add_command(label="Salir", command=quit)
        menuBar.add_cascade(label="Jugar", menu=playMenu)

        modo = tk.Menu(master=menuBar)
        modo.add_command(
            label="H-H",
            # command=self.resetBoard
        )
        modo.add_separator()
        modo.add_command(
            label="H-M",
            # command=self.resetBoard
        )
        menuBar.add_cascade(label="modo", menu=modo)


    def resetBoard(self):
        """Reset the game's board to play again."""
        self._gameController.resetGame()
        self._updateDisplay(msg="¿Empezamos?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")