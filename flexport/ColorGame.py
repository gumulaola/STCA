class Game:
    def __init__(self):
        self.my_dict = {}
        self.my_peek = {}

    def put(self, color, index):
        if index not in self.my_dict:
            self.my_dict[index] = color
            self.my_peek[index] = [color, 1]
        else:
            cur_peek = self.my_peek[index]
            cur_peek_color, cur_peek_ctn = cur_peek
            self.my_dict[index] += color
            if color != cur_peek_color:
                self.my_peek[index] = [color, 1]
            else:
                self.my_peek[index] = [color, cur_peek_ctn+1]
                if cur_peek_ctn == 3:
                    return True
        return False


ins = Game()
print(ins.put("R", 1))
print(ins.put("R", 1))
print(ins.put("R", 1))
print(ins.put("C", 2))
print(ins.put("R", 2))
print(ins.put("C", 2))
print(ins.put("C", 2))
print(ins.put("C", 2))
print(ins.put("C", 2))
