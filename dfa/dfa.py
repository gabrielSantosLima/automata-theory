class State:
    def __init__(self, label: str):
        self.label = label

class DFA:
    def __init__(self, q: list[State], Σ: list[str], δ, q0: int, f: list[int]):
        self.q = q
        self.Σ = Σ
        self.δ = δ
        self.q0 = q0
        self.f = f
    
    def compute(self, w: str) -> bool:
        current_state_index = self.q0
        for a in range(len(w)):
            current_state_index = self.δ(current_state_index, w[a])
            if current_state_index == None:
                return False
        return current_state_index in self.f

def δ1(state_index: int, symbol: str) -> int| None:
    transactions = {
        (0,"0"): 0,
        (0,"1"): 1,
        (1,"0"): 2,
        (1,"1"): 1,
        (2,"0"): 1,
        (2,"1"): 1,
    }
    key = (state_index, symbol)
    return transactions[key] if key in transactions else None


def main():
    q = [State('q0'), State('q1'), State('q2')]
    f = [1]
    Σ = ['0', '1']
    q0 = 0
    dfa = DFA(q, Σ, δ1, q0, f)

    print(f"011 {'accept' if dfa.compute('011') else 'reject'}.") # should accept
    print(f"0101 {'accept' if dfa.compute('0101') else 'reject'}.") # should accept
    print(f"0 {'accept' if dfa.compute('0') else 'reject'}.") # should reject
    print(f"000000000 {'accept' if dfa.compute('000000000') else 'reject'}.") # should reject
    print(f"010 {'accept' if dfa.compute('010') else 'reject'}.") # should reject
    print(f"'' {'accept' if dfa.compute('') else 'reject'}.") # should reject

main()