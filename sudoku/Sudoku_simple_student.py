# Note: Implementation of naked twins strategy and diagonal constraint propagation
# based on Udacity AIND 'Solving a Sudoku using AI' lecture notes

# encoding the board
rows = 'ABCDEFGHI'
cols = '123456789'
import matplotlib.pyplot as plt


# Cross funtzioak, 2 String-en arteko konbinazio guztiak itzultzen dizkigu, lista batean:
# adibidez: a='AB' eta b='CD' badira, cross(a,b)-k ['AC','AD','BC','BD'] itzuliko digu
def cross(a, b):
    return [s + t for s in a for t in b]


# Hiztegia aktualizatzeko balio du
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    return values


# grid_values funtzioak, sarrerako string formatuko sudokua, dikzionario formatura pasatuko du. eta balio denak erantsiko dizkio
def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.
    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))


# Sudokua erakutsiko digu, komando linean
def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    if not values:
        print('fail')
        exit()
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    return


##----------------------------------------------------------------------------
# sudokua egiteko metodoak
# http://humage.com/blogs/basic-advanced-sudoku-elimination-techniques-to-solve-sudoku-puzzles.html
##----------------------------------------------------------------------------

# 1 Eliminate: Begiratu Unitate bakoitzean dauden datuak, eta kendu unitatea konpartitzen duten gelaxketatik, balio horiek

def eliminate(values):
    """Eliminate values from peers of each box with a single value.
    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.
    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """



# 2 Only_choice: aukera bakarra dauzkaten gelaxkak, gure sudokuko hiztegian sartu

def only_choice(values):
    """Finalize all values that are the only choice for a unit.
    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.
    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """


# 3- Naked twins:

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """


# -------------------------------------------------------------------------
# Solverra
# oraingoz, estragegia, eliminate + only_choice + NakedTwins egitea da. hau da, problema txikitzen joatea
# -----------------------------------------------------------------------
def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    puzzle = grid_values(grid)
    # solve the puzzle
    values = reduce_puzzle(puzzle)
    if all(len(values[s]) == 1 for s in boxes):
        return values  # Solved!
    else:
        return False


# Sudokua erakutsiko digu, taula gisa
def display_plt(sudoku):
    mat = []
    line = []
    for c in sudoku:
        line.append(sudoku[c])
        if len(line) >= 9:
            mat.append(line)
            line = []
    fig, ax = plt.subplots()
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    ax.table(cellText=mat, loc='center')

    fig.tight_layout()

    plt.show()


# encoding the board
rows = 'ABCDEFGHI'
cols = '123456789'
# sortu gelaxka guztiak
boxes = cross(rows, cols)
# sortu  unitateak (errenkada, zutabe eta karratuak)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
# juntatu unitate guztiak lista bakarreak
unitlist = row_units + column_units + square_units
# gelaxka bakoitza zein unitatetan egon daitekeen esango digun hiztegi bat sortuko dugu
# giltza/key-a gelaxka identifikatzailea izango da, eta balioa, gelaxka hori dituen unitate guztiak
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
# gelaxka bakoitza zein beste gelaxkarekin interkonektatuta esango digun hiztegia egingo dugu
# giltza gelaxka identifikatzailea izango da, balioa, gelaxka horrekin unitaterenbat konpartitzen duen gelaxakren izena
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)

diag_sudoku_grid = '6.54.937..2......51.9235.....8....4..6.7.2.1..3....8.....5784.99......3..476.35.1'  # searchNecesary:'2...................1....7...6..8...3...9...7...6..4...4....8....52.............3'  onlyReduce: '6.54.937..2......51.9235.....8....4..6.7.2.1..3....8.....5784.99......3..476.35.1'
solution = solve(diag_sudoku_grid)
if solution:
    display_plt(solution)
else:
    print('too hard for me')
