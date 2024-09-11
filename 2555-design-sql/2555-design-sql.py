class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        for name in names:
            self.tables[name] = {}
        self.auto_incr = collections.Counter()

        

    def insertRow(self, name: str, row: List[str]) -> None:
        self.auto_incr[name] += 1
        rid = self.auto_incr[name]
        self.tables[name][rid] = row
        

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.tables[name][rowId]
        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId-1]
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)