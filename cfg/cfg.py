class CFG:
    def __init__(self, v: list[str], Σ: list[str], r: dict[str, list[str]], s: str):
        self.v = v
        self.Σ = Σ
        self.r = r
        self.s = s
        self.__w = s
    
    def __apply_rule__(self, w: str, rule: str, rule_index = 0) -> str:
        terminal_vars = self.r[rule][rule_index]
        return w.replace(rule, terminal_vars)

    def generate(self, rule: str, rule_index = 0) -> 'CFG':
        self.__w = self.__apply_rule__(self.__w, rule, rule_index)
        return self

    def get(self) -> str:
        w = self.__w
        self.__w = self.s
        return w
    
def main():
    r = {
        "A": ['0A1', 'B'],
        "B": ['#']
    }
    cfg = CFG(['A', 'B'], ['0', '1', '#'],  r, 'A')
    
    w = cfg.generate('A') \
        .generate('A') \
        .generate('A') \
        .generate('A', 1) \
        .generate('B') \
        .get()
    print(w) # should print "000#111"

main()