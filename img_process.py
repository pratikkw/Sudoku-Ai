import cv2
import numpy as np
import os

def extract_sudoku_cells(sudoku_grid):
    """
    Splits a Sudoku grid image into 9x9 individual cells and saves each cell as an image.
    :param sudoku_grid: Extracted and preprocessed Sudoku grid image
    :return: A 9x9 list of cell images
    """
    grid_size = sudoku_grid.shape[0]  # Assuming square grid
    cell_size = grid_size // 9  # Size of each cell
    
    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            x, y = j * cell_size, i * cell_size
            cell = sudoku_grid[y:y+cell_size, x:x+cell_size]  # Extract cell
            row.append(cell)
            
            # Save each cell as an image
            cell_filename = f"DIGIT/cell_{i}{j}.png"
            cv2.imwrite(cell_filename, cell)
        cells.append(row)
    
    return cells

# Example usage:
sudoku_grid = cv2.imread("122__ext-sdk.jpg", cv2.IMREAD_GRAYSCALE)
# cells = extract_sudoku_cells(sudoku_grid)
# cv2.imshow("Sample Cell", cells[0][0])  # Display top-left cell
# cv2.waitKey(0)
# cv2.destroyAllWindows()
extract_sudoku_cells(sudoku_grid)
