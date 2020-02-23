import core.globals
import remi

# USED FOR EVERYTHING WHICH DOESN'T FIT ANYWHERE ELSE

def generateTable(tableName='dummy', tableWidth='90%', noRows=1, noColumns=1, tableStyle={}, rowStyle={}, cellStyle={}, testmode=True):
    # Returns a Dict of elements of the table. The key foirmat in Dict:
    # TABLENAME-ROW-COL, e.g.    'mytable-003-004'    Row 3, Column 4 (with option noZerofill = 3)

    table = {}

    table[tableName] = remi.gui.Table(width=tableWidth, style=tableStyle)

    n = 1

    while n <= noRows:

        table[tableName + '-r' + str(n)] = remi.gui.TableRow(style=rowStyle)

        i = 1

        while i <= noColumns:

            if testmode == True:
                cellContent = tableName + '-' + str(n) + ',' + str(i)
            else:
                cellContent = ''

            table[tableName + '-' + str(n) + ',' + str(i)] = remi.gui.TableItem(cellContent, style=cellStyle)
            table[tableName + '-r' + str(n)].append(table[tableName + '-' + str(n) + ',' + str(i)])
            i = i + 1

        table[tableName].append(table[tableName + '-r' + str(n)])
        n = n + 1

    return table

