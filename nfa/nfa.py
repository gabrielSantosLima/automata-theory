class State:
    def __init__(self, label: str):
        self.label = label

class NFA:
    def __init__(self, q: list[State], Σ: list[str], δ, q0: int, f: list[int]):
        self.q = q
        self.Σ = Σ
        self.δ = δ
        self.q0 = q0
        self.f = f
    
    def __filter_states(self, current_processing: list[int], states: list[int]) -> list[int]:
        # filtering a state that has not yet been reached.
        return list(filter(lambda state: state not in current_processing, states))

    def compute(self, w: str) -> bool:
        # initializing processing in q0
        processing = [self.q0]
        for a in w:
            current_processing = []
            # each symbol is computed (stack-based processing)
            while len(processing) > 0:
                current_state = processing.pop()
                next_states = self.δ(current_state, a)
                # adding states not yet reached
                if next_states != None:
                    current_processing += self.__filter_states(current_processing, next_states)
            # for each state we have to verify if it has a lambda transaction for some state
            index = 0
            while index != len(current_processing):
                current_state = current_processing[index]
                lambda_state = self.δ(current_state, 'λ')
                current_processing += self.__filter_states(current_processing, lambda_state)
                index+=1
            # verifying the empty processing case: when it has any states to compute
            if len(current_processing) == 0:
                return False
            processing = current_processing.copy()
        # finally, if it has at least one final state, w is accepted. 
        for final_state in self.f:
            if final_state in processing:
                return True
        return False
    
    def compute_str(self, w:str):
        return 'accept' if self.compute(w) else 'reject'
                    
def δ1(state_index: int, symbol: str) -> list[int]:
    transactions = {
        (0,"0"): [0],
        (0,"1"): [0,1],
        (1,"0"): [2],
        (1,"λ"): [2],
        (2,"1"): [3],
        (3,"0"): [3],
        (3,"1"): [3],
    }
    key = (state_index, symbol)
    return transactions[key] if key in transactions else []

def main():
    q = [State('q1'), State('q2'), State('q3'), State('q4')]
    f = [3]
    Σ = ['0', '1']
    q0 = 0
    dfa = NFA(q, Σ, δ1, q0, f)

    print(f"011 {dfa.compute_str('011')}.") # should accept
    print(f"0111111111111 {dfa.compute_str('0111111111111')}.") # should accept
    print(f"010110 {dfa.compute_str('010110')}.") # should accept
    print(f"01 {dfa.compute_str('01')}.") # should reject
    print(f"0 {dfa.compute_str('0')}.") # should reject
    print(f"'' {dfa.compute_str('')}.") # should reject

main()