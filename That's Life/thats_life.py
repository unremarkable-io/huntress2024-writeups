from collections import namedtuple

from gameoflife_protobuf.gameoflife_pb2 import Grid, CellRow, Cell

"""
% ./protoc --decode_raw < game_state.pb

------------------------------------------------------------------------------------------------------------------------

https://arkadiyt.com/2024/03/03/reverse-engineering-protobuf-definitiions-from-compiled-binaries/
https://github.com/arkadiyt/protodump

% go install github.com/arkadiyt/protodump/cmd/protodump@latest

% ~/go/bin/protodump -file gameoflife -output dumped
Wrote dumped/github.com/HuskyHacks/thats_life/pb/gameoflife.proto

% mv dumped/github.com/HuskyHacks/thats_life/pb/gameoflife.proto ./

% ./protoc --python_out=gameoflife_protobuf --pyi_out=gameoflife_protobuf gameoflife.proto

% ./protoc --decode=thats_life.Grid ./gameoflife.proto < win_grid.pb
"""

Coords = namedtuple('Coords', ['y', 'x'])
CellData = namedtuple('CellData', ['color', 'alive'])

win_criteria = {
    Coords(10, 15): CellData(31, True), Coords(20, 25): CellData(32, True), Coords(30, 35): CellData(33, True),
    Coords(40, 45): CellData(34, True), Coords(25, 50): CellData(35, True), Coords(5, 55): CellData(36, True),
    Coords(15, 60): CellData(37, True), Coords(35, 65): CellData(31, True), Coords(45, 70): CellData(32, True),
    Coords(0, 75): CellData(33, True), Coords(1, 80): CellData(34, True), Coords(2, 85): CellData(35, True)
}


def generate_win_grid():
    grid = Grid()
    grid.width = 400
    grid.height = 50

    for row_number in range(grid.height):
        cell_row = CellRow()
        for column_number in range(grid.width):
            coords = Coords(y=row_number, x=column_number)
            cell = Cell()
            if coords in win_criteria:
                cell = Cell(alive=win_criteria[coords].alive, color=win_criteria[coords].color)
            cell_row.cells.append(cell)
        grid.rows.append(cell_row)

    with open('win_grid.pb', 'wb') as f:
        f.write(grid.SerializeToString())


def main():
    generate_win_grid()


if __name__ == '__main__':
    main()
