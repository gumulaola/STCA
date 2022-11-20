class CardPay:
    def __init__(self, A, B, C):
        self.balance = [A, B, C]

    def can(self, arr):
        for i in range(arr):
            if arr[i] > self.balance[i]:
                return False

        return True

    def buy(self, arr):
        if not self.can(arr):
            return -1
        else:
            for i in range(arr):
                self.balance[i] -= self.arr[i]
            return self.balance
