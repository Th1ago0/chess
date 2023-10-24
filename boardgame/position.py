class Position:
    def __init__(self, row, column):
        self.row = row;
        self.column = column;
        
    def str(self):
        return f"{self.row}, {self.column}";
        
    def set_row(self, row):
        self.row = row;
        
    def get_row(self):
        return self.row
        
    def set_column(self, column):
        self.column = column;
        
    def get_column(self):
        return self.column;
