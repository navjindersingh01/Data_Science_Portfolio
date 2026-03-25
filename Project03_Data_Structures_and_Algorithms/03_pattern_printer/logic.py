class Patterns:
    def __init__(self,num):
        self.num = num
    
    def pyramid(self):
        row = []
        for i in range(1,self.num+1):
            row.append(" " * (self.num - i) + "*" * (2*i - 1))
        return "\n".join(row)
    
    def inverse_pyramid(self):
        row = []
        for i in range(self.num,0,-1):
            row.append(" " * (self.num - i) + "*" * (2*i - 1))
        return "\n".join(row)

    def right_triangle(self):
        row = []
        for i in range(1, self.num+1):
            row.append("*" * i)
        return "\n".join(row)
    
    def inverse_right_triangle(self):
        row = []
        for i in range(self.num,0,-1):
            row.append("*"*i)
        return "\n".join(row)
    
    def diamond(self):
        row = []
        row.append(self.pyramid())
        row.append(self.inverse_pyramid())

        return "\n".join(row)