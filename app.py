from flask import Flask, Response, request

app = Flask(__name__)

def move_possible(grid, move):
    # Check if a move is possible by scanning the grid for movable tiles
    for i in range(4):
        for j in range(4):
            if grid[i][j]:
                if move == '0' and i > 0 and (grid[i-1][j] == 0 or grid[i-1][j] == grid[i][j]):
                    return True  # Up
                if move == '1' and j < 3 and (grid[i][j+1] == 0 or grid[i][j+1] == grid[i][j]):
                    return True  # Right
                if move == '2' and i < 3 and (grid[i+1][j] == 0 or grid[i+1][j] == grid[i][j]):
                    return True  # Down
                if move == '3' and j > 0 and (grid[i][j-1] == 0 or grid[i][j-1] == grid[i][j]):
                    return True  # Left
    return False

@app.route("/")
def index():
    state = request.args.get("state")
    flat_grid = list(map(int, state.split(",")))
    # Convert from column-major to row-major order
    grid = [flat_grid[i::4] for i in range(4)]

    preferred_moves = ['2', '3', '1', '0']  # Down, Left, Right, Up

    for move in preferred_moves:
        if move_possible(grid, move):
            return Response(move, headers={"access-control-allow-origin": "*"})
    # If no valid moves, return a default move
    return Response('0', headers={"access-control-allow-origin": "*"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

