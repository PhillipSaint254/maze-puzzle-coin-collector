class CoinCollector():

    # PART 1
    def findMaxCoinsTopDown(startRow, startCol):

        maze, rows, cols = readMazeFromFile('maze.txt')

        # Initialize all position with a -1 as a default value for fall back
        data_points = [[-1 for i in range(cols)] for j in range(rows)]
        # Initialize the start position with actual values in the maze
        data_points[startRow][startCol] = int(
            maze[startRow][startCol]) if maze[startRow][startCol].isdigit() else 0

        # adding correct values for all values to the right of the starting position
        for col in range(startCol+1, cols):
            if maze[startRow][col] == 'x':
                data_points[startRow][col] = -1
            else:
                data_points[startRow][col] = data_points[startRow][col - 1] + \
                    (int(maze[startRow][col])
                     if maze[startRow][col].isdigit() else 0)

        # adding correct values for all values to the bottom of the startig position
        for row in range(startRow+1, rows):
            if maze[row][startCol] == 'x':
                data_points[row][startCol] = -1
            else:
                data_points[row][startCol] = data_points[row - 1][startCol] + \
                    (int(maze[row][startCol]) if maze[row]
                     [startCol].isdigit() else 0)

        for row in range(startRow+1, rows):
            for col in range(startCol+1, cols):
                if maze[row][col] != 'x':
                    # calculate coins collected from the North-South movement
                    coins_from_top = data_points[row -
                                                 1][col] if data_points[row - 1][col] != -1 else -1

                    # calcilate coins collected from the West-East movement
                    coins_from_left = data_points[row][col -
                                                       1] if data_points[row][col - 1] != -1 else -1

                    # Calculate the maximum coin collected between the two routes and keep the route with the most coins
                    # default to 0 if no coin is collected
                    if coins_from_top != -1 or coins_from_left != -1:
                        data_points[row][col] = max(coins_from_top, coins_from_left) + (
                            int(maze[row][col]) if maze[row][col].isdigit() else 0)

        return data_points[-1][-1] if data_points[-1][-1] > 0 else -1

    # PART 2
    def findMaxCoinsBottomUp(startRow, startCol):

        maze, rows, cols = readMazeFromFile('maze.txt')

        # start by initializing data points with -1 as the default value for fall back
        data_points = [[-1 for i in range(cols)] for j in range(rows)]
        # Assign default values for the end position in the maze thus botom-up
        data_points[-1][-1] = int(maze[-1][-1]
                                  ) if maze[-1][-1].isdigit() else 0

        # calculation of correct values to the left of the ending position upto the starting column
        for col in range(cols-2, startCol-1, -1):
            if maze[-1][col] == 'x':
                data_points[-1][col] = -1
            else:
                data_points[-1][col] = data_points[-1][col + 1] + \
                    (int(maze[-1][col]) if maze[-1][col].isdigit() else 0)

        # calculation of the correct values above the end postion upto the starting row
        for row in range(rows-2, startRow-1, -1):
            if maze[row-1][-1] == 'x':
                maze[row-1][-1] = -1
            else:
                data_points[row][-1] = data_points[row + 1][-1] + \
                    (int(maze[row][-1]) if maze[row]
                     [-1].isdigit() else 0)

        for row in range(rows-2, startRow-1, -1):
            for col in range(cols-2, startCol-1, -1):
                if maze[row][col] != 'x':
                    coins_from_bottom = data_points[row +
                                                    1][col] if data_points[row + 1][col] != -1 else -1
                    coins_from_right = data_points[row][col +
                                                        1] if data_points[row][col + 1] != -1 else -1
                    if coins_from_bottom != -1 or coins_from_right != -1:
                        data_points[row][col] = max(coins_from_bottom, coins_from_right) + (
                            int(maze[row][col]) if maze[row][col].isdigit() else 0)

        return data_points[startRow][startCol] if data_points[startRow][startCol] > 0 else -1


def readMazeFromFile(file_name):
    with open(file_name, 'r') as file:
        rows = int(file.readline().strip())
        cols = int(file.readline().strip())
        maze = []
        for line in file.readlines():
            list_item = [item for item in list(line) if item != '\n']
            list_item += [' ' for _ in range(5 - len(list_item))]
            maze.append(list_item)
    return maze, rows, cols


startRow = int(input("Enter starting row: "))
startCol = int(input("Enter starting column: "))

print(CoinCollector.findMaxCoinsTopDown(startRow, startCol))
print(CoinCollector.findMaxCoinsBottomUp(startRow, startCol))
