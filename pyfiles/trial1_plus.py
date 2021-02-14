class Plus:
    def __init__(self, conf):
        self.a = conf["a"]
        self.b = conf["b"]

    def execute(self):
        self.plus_res = self.a + self.b
        return self.plus_res