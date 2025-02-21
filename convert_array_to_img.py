import matplotlib.pyplot as plt
import os

UPLOAD_FOLDER = "static/solution/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def draw_sudoku(board, filename=None):
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Draw grid lines
    for i in range(10):
        lw = 2 if i % 3 == 0 else 0.5
        ax.plot([0, 9], [i, i], 'k', lw=lw)
        ax.plot([i, i], [0, 9], 'k', lw=lw)

    # Fill in the numbers
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                ax.text(col + 0.5, 8.5 - row, str(num), ha='center', va='center', fontsize=14)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    ax.set_frame_on(False)
    
    if filename:
        
        for filename in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            if(os.path.isfile(file_path)):
                os.remove(file_path)

        plt.savefig(f"{UPLOAD_FOLDER}/{filename}", bbox_inches='tight', dpi=300)  # Save as an image
    else:
        plt.show()  # Display the image

# Example usage
sudoku_puzzle = [
    [9, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

draw_sudoku(sudoku_puzzle, "sudoku_solution.png")  # Save as "sudoku_grid.png"
