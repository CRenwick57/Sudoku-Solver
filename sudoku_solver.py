#TODO: Add a front end so I don't have to painstakingly type out an entire 81 character string every time

from datetime import datetime

EASY = '704000000053407200600305970000500498045630000791400500016859240000020360047006000'
MEDIUM = '073000100000002006060050200600000000007010000045806000000000045300500070080009320'
HARD = '080000000020100000560007000050007090090800010408003050204060000000085200800000100'
VHARD = '600040002090007800007100050800000030000070000090000008050004900002500030300020004'

class Cell(object):

    def __init__(self, value = None):
        self.value = value
        self.possible = [1,2,3,4,5,6,7,8,9]

    def removePossibility(self, n):
        if not self.value and n in self.possible:
            self.possible.remove(n)

    def setValue(self, n):
        if not self.value:
            self.value = n
            self.possible = []

    def __str__(self):
        res = self.name
        if self.value:
            res+=','+str(self.value)
        return res

class Solver(object):
    '''game layout:
    A1 A2 A3 | B1 B2 B3 | C1 C2 C3
    A4 A5 A6 | B4 B5 B6 | C4 C5 C6
    A7 A8 A9 | B7 B8 B9 | C7 C8 C9
    -------------------------------
    D1 D2 D3 | E1 E2 E3 | F1 F2 F3
    D4 D5 D6 | E4 E5 E6 | F4 F5 F6
    D7 D8 D9 | E7 E8 E9 | F6 F7 F8
    -------------------------------
    G1 G2 G3 | H1 H2 H3 | I1 I2 I3
    G4 G5 G6 | H4 H5 H6 | I4 I5 I6
    G7 G8 G9 | H7 H8 H9 | I7 I8 I9
    Rows labelled R1-R9 from top to bottom
    Columns labelled L1-L9 from left to right
    Boxes labeled A-I as above
    Cell values entered into the solver in box order 1-9
    '''
    def __init__(self, game):
        if type(game) is int:
            game = str(game)
        if type(game) is str:
            game = list(game)
        self.game = game
        self.A1 = Cell()
        self.A2 = Cell()
        self.A3 = Cell()
        self.A4 = Cell()
        self.A5 = Cell()
        self.A6 = Cell()
        self.A7 = Cell()
        self.A8 = Cell()
        self.A9 = Cell()
        self.B1 = Cell()
        self.B2 = Cell()
        self.B3 = Cell()
        self.B4 = Cell()
        self.B5 = Cell()
        self.B6 = Cell()
        self.B7 = Cell()
        self.B8 = Cell()
        self.B9 = Cell()
        self.C1 = Cell()
        self.C2 = Cell()
        self.C3 = Cell()
        self.C4 = Cell()
        self.C5 = Cell()
        self.C6 = Cell()
        self.C7 = Cell()
        self.C8 = Cell()
        self.C9 = Cell()
        self.D1 = Cell()
        self.D2 = Cell()
        self.D3 = Cell()
        self.D4 = Cell()
        self.D5 = Cell()
        self.D6 = Cell()
        self.D7 = Cell()
        self.D8 = Cell()
        self.D9 = Cell()
        self.E1 = Cell()
        self.E2 = Cell()
        self.E3 = Cell()
        self.E4 = Cell()
        self.E5 = Cell()
        self.E6 = Cell()
        self.E7 = Cell()
        self.E8 = Cell()
        self.E9 = Cell()
        self.F1 = Cell()
        self.F2 = Cell()
        self.F3 = Cell()
        self.F4 = Cell()
        self.F5 = Cell()
        self.F6 = Cell()
        self.F7 = Cell()
        self.F8 = Cell()
        self.F9 = Cell()
        self.G1 = Cell()
        self.G2 = Cell()
        self.G3 = Cell()
        self.G4 = Cell()
        self.G5 = Cell()
        self.G6 = Cell()
        self.G7 = Cell()
        self.G8 = Cell()
        self.G9 = Cell()
        self.H1 = Cell()
        self.H2 = Cell()
        self.H3 = Cell()
        self.H4 = Cell()
        self.H5 = Cell()
        self.H6 = Cell()
        self.H7 = Cell()
        self.H8 = Cell()
        self.H9 = Cell()
        self.I1 = Cell()
        self.I2 = Cell()
        self.I3 = Cell()
        self.I4 = Cell()
        self.I5 = Cell()
        self.I6 = Cell()
        self.I7 = Cell()
        self.I8 = Cell()
        self.I9 = Cell()
        self.row1 = [self.A1,self.A2,self.A3,self.B1,self.B2,self.B3,self.C1,self.C2,self.C3]
        self.row2 = [self.A4,self.A5,self.A6,self.B4,self.B5,self.B6,self.C4,self.C5,self.C6]
        self.row3 = [self.A7,self.A8,self.A9,self.B7,self.B8,self.B9,self.C7,self.C8,self.C9]
        self.row4 = [self.D1,self.D2,self.D3,self.E1,self.E2,self.E3,self.F1,self.F2,self.F3]
        self.row5 = [self.D4,self.D5,self.D6,self.E4,self.E5,self.E6,self.F4,self.F5,self.F6]
        self.row6 = [self.D7,self.D8,self.D9,self.E7,self.E8,self.E9,self.F7,self.F8,self.F9]
        self.row7 = [self.G1,self.G2,self.G3,self.H1,self.H2,self.H3,self.I1,self.I2,self.I3]
        self.row8 = [self.G4,self.G5,self.G6,self.H4,self.H5,self.H6,self.I4,self.I5,self.I6]
        self.row9 = [self.G7,self.G8,self.G9,self.H7,self.H8,self.H9,self.I7,self.I8,self.I9]

        self.col1 = [self.A1,self.A4,self.A7,self.D1,self.D4,self.D7,self.G1,self.G4,self.G7]
        self.col2 = [self.A2,self.A5,self.A8,self.D2,self.D5,self.D8,self.G2,self.G5,self.G8]
        self.col3 = [self.A3,self.A6,self.A9,self.D3,self.D6,self.D9,self.G3,self.G6,self.G9]
        self.col4 = [self.B1,self.B4,self.B7,self.E1,self.E4,self.E7,self.H1,self.H4,self.H7]
        self.col5 = [self.B2,self.B5,self.B8,self.E2,self.E5,self.E8,self.H2,self.H5,self.H8]
        self.col6 = [self.B3,self.B6,self.B9,self.E3,self.E6,self.E9,self.H3,self.H6,self.H9]
        self.col7 = [self.C1,self.C4,self.C7,self.F1,self.F4,self.F7,self.I1,self.I4,self.I7]
        self.col8 = [self.C2,self.C5,self.C8,self.F2,self.F5,self.F8,self.I2,self.I5,self.I8]
        self.col9 = [self.C3,self.C6,self.C9,self.F3,self.F6,self.F9,self.I3,self.I6,self.I9]

        self.boxA = [self.A1,self.A2,self.A3,self.A4,self.A5,self.A6,self.A7,self.A8,self.A9]
        self.boxB = [self.B1,self.B2,self.B3,self.B4,self.B5,self.B6,self.B7,self.B8,self.B9]
        self.boxC = [self.C1,self.C2,self.C3,self.C4,self.C5,self.C6,self.C7,self.C8,self.C9]
        self.boxD = [self.D1,self.D2,self.D3,self.D4,self.D5,self.D6,self.D7,self.D8,self.D9]
        self.boxE = [self.E1,self.E2,self.E3,self.E4,self.E5,self.E6,self.E7,self.E8,self.E9]
        self.boxF = [self.F1,self.F2,self.F3,self.F4,self.F5,self.F6,self.F7,self.F8,self.F9]
        self.boxG = [self.G1,self.G2,self.G3,self.G4,self.G5,self.G6,self.G7,self.G8,self.G9]
        self.boxH = [self.H1,self.H2,self.H3,self.H4,self.H5,self.H6,self.H7,self.H8,self.H9]
        self.boxI = [self.I1,self.I2,self.I3,self.I4,self.I5,self.I6,self.I7,self.I8,self.I9]

        self.rows = [self.row1,self.row2,self.row3,self.row4,self.row5,self.row6,self.row7,self.row8,self.row9]
        self.cols = [self.col1,self.col2,self.col3,self.col4,self.col5,self.col6,self.col7,self.col8,self.col9]
        self.boxes = [self.boxA,self.boxB,self.boxC,self.boxD,self.boxE,self.boxF,self.boxG,self.boxH,self.boxI]

        self.cells = []
        for box in self.boxes:
            self.cells.extend(box)

    def checkSolved(self):
        for cell in self.cells:
            if not cell.value:
                return False
        return True

    def inRowOrColInBox(self, box):
        topRow = [box[0],box[1],box[2]]
        midRow = [box[3],box[4],box[5]]
        botRow = [box[6],box[7],box[8]]
        leftCol = [box[0],box[3],box[6]]
        midCol = [box[1],box[4],box[7]]
        rightCol = [box[2],box[5],box[8]]
        boxRows = [topRow,midRow,botRow]
        boxCols = [leftCol,midCol,rightCol]
        topRowPos = []
        midRowPos = []
        botRowPos = []
        leftColPos = []
        midColPos = []
        rightColPos = []
        boxRowPos = [topRowPos,midRowPos,botRowPos]
        boxColPos = [leftColPos,midColPos,rightColPos]
        for i in range(3):
            for cell in boxRows[i]:
                boxRowPos[i].extend(cell.possible)
            for cell in boxCols[i]:
                boxColPos[i].extend(cell.possible)
        for i in range(1,10):
            ic = 0
            for rp in boxRowPos:
                if i in rp:
                    ic+=1
            if ic == 1:
                for j in range(3):
                    if i in boxRowPos[j]:
                        c = boxRows[j][0]
                        for row in self.rows:
                            if c in row:
                                for cell in row:
                                    if cell not in box:
                                        cell.removePossibility(i)
            ic = 0
            for cp in boxColPos:
                if i in cp:
                    ic+=1
            if ic == 1:
                for j in range(3):
                    if i in boxColPos[j]:
                        c = boxCols[j][0]
                        for col in self.cols:
                            if c in col:
                                for cell in col:
                                    if cell not in box:
                                        cell.removePossibility(i)

    def inBoxInRow(self, row):
        leftBox = [row[0],row[1],row[2]]
        midBox = [row[3],row[4],row[5]]
        rightBox = [row[6],row[7],row[8]]
        rowBoxes = [leftBox,midBox,rightBox]
        leftBoxPos = []
        midBoxPos = []
        rightBoxPos = []
        rowBoxPos = [leftBoxPos,midBoxPos,rightBoxPos]
        for i in range(3):
            for cell in rowBoxes[i]:
                rowBoxPos[i].extend(cell.possible)
        for i in range(1,10):
            ic = 0
            for bp in rowBoxPos:
                if i in bp:
                    ic+=1
            if ic == 1:
                for j in range(3):
                    if i in rowBoxPos[j]:
                        c = rowBoxes[j][0]
                        for box in self.boxes:
                            if c in box:
                                for cell in box:
                                    if cell not in row:
                                        cell.removePossibility(i)

    def inBoxInCol(self,col):
        leftBox = [col[0],col[1],col[2]]
        midBox = [col[3],col[4],col[5]]
        rightBox = [col[6],col[7],col[8]]
        colBoxes = [leftBox,midBox,rightBox]
        leftBoxPos = []
        midBoxPos = []
        rightBoxPos = []
        colBoxPos = [leftBoxPos,midBoxPos,rightBoxPos]
        for i in range(3):
            for cell in colBoxes[i]:
                colBoxPos[i].extend(cell.possible)
        for i in range(1,10):
            ic = 0
            for bp in colBoxPos:
                if i in bp:
                    ic+=1
            if ic == 1:
                for j in range(3):
                    if i in colBoxPos[j]:
                        c = colBoxes[j][0]
                        for box in self.boxes:
                            if c in box:
                                for cell in box:
                                    if cell not in col:
                                        cell.removePossibility(i)

    def checkPairs(self, brc):
        possible = []
        for cell in brc:
            possible.extend(cell.possible)
        potentials = []
        for i in range(1,10):
            if possible.count(i) == 2:
                potentials.append(i)
        pairs = []
        for p in potentials:
            pair = []
            for cell in brc:
                if p in cell.possible:
                    pair.append(cell)
            pairs.append(pair)
        truePairs = {}
        for i in range(len(pairs)):
            if pairs.count(pairs[i]) == 2:
                if tuple(pairs[i]) in truePairs:
                    truePairs[tuple(pairs[i])].append(potentials[i])
                else:
                    truePairs[tuple(pairs[i])] = [potentials[i]]
        for k,v in truePairs.items():
            for cell in k:
                for i in range(1,10):
                    if i not in v:
                        cell.removePossibility(i)

    def xWing(self, rc, ROW=True):
        possible = []
        for cell in rc:
            possible.extend(cell.possible)
        pairs = []
        for i in range(1,10):
            if possible.count(i) == 2:
                pairs.append(i)
        pairDict = {}
        for p in pairs:
            pairDict[p] = []
            for i in range(9):
                if p in rc[i].possible:
                    pairDict[p].append(i)
        if ROW:
            for num,cells in pairDict.items():
                for row in self.rows:
                    if row != rc:
                        rowPoss = []
                        for cell in row:
                            rowPoss.extend(cell.possible)
                        if rowPoss.count(num) == 2:
                            if num in row[cells[0]].possible and num in row[cells[1]].possible:
                                markedCells = [rc[cells[0]],rc[cells[1]],row[cells[0]],row[cells[1]]]
                                for col in self.cols:
                                    if markedCells[0] in col or markedCells[1] in col:
                                        for cell in col:
                                            if cell not in markedCells:
                                                cell.removePossibility(num)
        else:
            for num,cells in pairDict.items():
                for col in self.cols:
                    if col != rc:
                        colPoss = []
                        for cell in col:
                            colPoss.extend(cell.possible)
                        if colPoss.count(num) == 2:
                            if num in col[cells[0]].possible and num in col[cells[1]].possible:
                                markedCells = [rc[cells[0]],rc[cells[1]],col[cells[0]],col[cells[1]]]
                                for row in self.rows:
                                    if markedCells[0] in row or markedCells[1] in row:
                                        for cell in row:
                                            if cell not in markedCells:
                                                cell.removePossibility(num)

    def setUpSolve(self):
        for i in range(81):
            if self.game[i] != '0':
                self.cells[i].setValue(int(self.game[i]))
                for row in self.rows:
                    if self.cells[i] in row:
                        for cell in row:
                            cell.removePossibility(int(self.game[i]))
                for col in self.cols:
                    if self.cells[i] in col:
                        for cell in col:
                            cell.removePossibility(int(self.game[i]))
                for box in self.boxes:
                    if self.cells[i] in box:
                        for cell in box:
                            cell.removePossibility(int(self.game[i]))

    def solve(self):
        self.setUpSolve()
        startTime = datetime.now()
        timeOut = False
        while not self.checkSolved() and not timeOut:
            for row in self.rows:
                pCount = [0,0,0,0,0,0,0,0,0]
                for cell in row:
                    if len(cell.possible) == 1:
                        val = cell.possible[0]
                        cell.setValue(val)
                        for xrow in self.rows:
                            if cell in xrow:
                                for c in xrow:
                                    c.removePossibility(val)
                        for xcol in self.cols:
                            if cell in xcol:
                                for c in xcol:
                                    c.removePossibility(val)
                        for xbox in self.boxes:
                            if cell in xbox:
                                for c in xbox:
                                    c.removePossibility(val)
                    else:
                        for p in cell.possible:
                            pCount[p-1]+=1
                for i in range(9):
                    if pCount[i] is 1:
                        j = i+1
                        for cell in row:
                            if j in cell.possible:
                                cell.setValue(j)
                                for xrow in self.rows:
                                    if cell in xrow:
                                        for c in xrow:
                                            c.removePossibility(j)
                                for xcol in self.cols:
                                    if cell in xcol:
                                        for c in xcol:
                                            c.removePossibility(j)
                                for xbox in self.boxes:
                                    if cell in xbox:
                                        for c in xbox:
                                            c.removePossibility(j)
                self.inBoxInRow(row)
                self.checkPairs(row)
                self.xWing(row,True)
            for col in self.cols:
                pCount = [0,0,0,0,0,0,0,0,0]
                for cell in col:
                    if len(cell.possible) == 1:
                        val = cell.possible[0]
                        cell.setValue(val)
                        for xrow in self.rows:
                            if cell in xrow:
                                for c in xrow:
                                    c.removePossibility(val)
                        for xcol in self.cols:
                            if cell in xcol:
                                for c in xcol:
                                    c.removePossibility(val)
                        for xbox in self.boxes:
                            if cell in xbox:
                                for c in xbox:
                                    c.removePossibility(val)
                    else:
                        for p in cell.possible:
                            pCount[p-1]+=1
                for i in range(9):
                    if pCount[i] is 1:
                        j = i+1
                        for cell in col:
                            if j in cell.possible:
                                cell.setValue(j)
                                for xrow in self.rows:
                                    if cell in xrow:
                                        for c in xrow:
                                            c.removePossibility(j)
                                for xcol in self.cols:
                                    if cell in xcol:
                                        for c in xcol:
                                            c.removePossibility(j)
                                for xbox in self.boxes:
                                    if cell in xbox:
                                        for c in xbox:
                                            c.removePossibility(j)
                self.inBoxInCol(col)
                self.checkPairs(col)
                self.xWing(col,False)
            for box in self.boxes:
                pCount = [0,0,0,0,0,0,0,0,0]
                for cell in box:
                    if len(cell.possible) == 1:
                        val = cell.possible[0]
                        cell.setValue(val)
                        for xrow in self.rows:
                            if cell in xrow:
                                for c in xrow:
                                    c.removePossibility(val)
                        for xcol in self.cols:
                            if cell in xcol:
                                for c in xcol:
                                    c.removePossibility(val)
                        for xbox in self.boxes:
                            if cell in xbox:
                                for c in xbox:
                                    c.removePossibility(val)
                    else:
                        for p in cell.possible:
                            pCount[p-1]+=1
                for i in range(9):
                    if pCount[i] is 1:
                        j = i+1
                        for cell in box:
                            if j in cell.possible:
                                cell.setValue(j)
                                for xrow in self.rows:
                                    if cell in xrow:
                                        for c in xrow:
                                            c.removePossibility(j)
                                for xcol in self.cols:
                                    if cell in xcol:
                                        for c in xcol:
                                            c.removePossibility(j)
                                for xbox in self.boxes:
                                    if cell in xbox:
                                        for c in xbox:
                                            c.removePossibility(j)
                self.inRowOrColInBox(box)
                self.checkPairs(box)
            timeOut = (datetime.now()-startTime).seconds >= 30
        if timeOut:
            return 'Solver Timed out'
        res = ''
        for cell in self.cells:
            res+=str(cell.value)
        return res

    def __str__(self):
        res = ''
        for row in self.rows:
            for cell in row:
                if cell.value:
                    res+=str(cell.value)
                else:
                    res+='_'
            res+='\n'
        return res

#sudoku = Solver('000000703007200000000405920001370200806000405003084600094802000000004600706000000')

#sudoku in this function should be a string like in the commented example above
def solveFormatted(sudoku):
    solver = Solver(sudoku)
    res = solver.solve()
    if res == 'Solver Timed out':
        return res
    r1 = res[0]+res[1]+res[2]+'|'+res[9]+res[10]+res[11]+'|'+res[18]+res[19]+res[20]+'\n'
    r2 = res[3]+res[4]+res[5]+'|'+res[12]+res[13]+res[14]+'|'+res[21]+res[22]+res[23]+'\n'
    r3 = res[6]+res[7]+res[8]+'|'+res[15]+res[16]+res[17]+'|'+res[24]+res[25]+res[26]+'\n'
    lb = '___________\n'
    r4 = res[27]+res[28]+res[29]+'|'+res[36]+res[37]+res[38]+'|'+res[45]+res[46]+res[47]+'\n'
    r5 = res[30]+res[31]+res[32]+'|'+res[39]+res[40]+res[41]+'|'+res[48]+res[49]+res[50]+'\n'
    r6 = res[33]+res[34]+res[35]+'|'+res[42]+res[43]+res[44]+'|'+res[51]+res[52]+res[53]+'\n'

    r7 = res[54]+res[55]+res[56]+'|'+res[63]+res[64]+res[65]+'|'+res[72]+res[73]+res[74]+'\n'
    r8 = res[57]+res[58]+res[59]+'|'+res[66]+res[67]+res[68]+'|'+res[75]+res[76]+res[77]+'\n'
    r9 = res[60]+res[61]+res[62]+'|'+res[69]+res[70]+res[71]+'|'+res[78]+res[79]+res[80]
    s = r1+r2+r3+lb+r4+r5+r6+lb+r7+r8+r9
    return s
