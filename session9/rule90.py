from template import AbstractSimulation

class Rule90(AbstractSimulation):

    _rules = {'111': '0', '110': '1', '101': '0', '100': '1', '011': '1', '010': '0', '001': '1', '000': '0'}

    def __init__(self, number_steps, initial_state=None):
        super().__init__(number_steps)

        if not initial_state:
            self.initial_state = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split()
        else:
            self.initial_state = initial_state

    def initialize_sim(self):
        self.state = self.initial_state
        self.time = 0

    def run_one_step(self):
        self.time += 1

        new_state = []

        for i in range(len(self.state)-2):
            stride = ''.join(self.state[i:i+3])
            window = self._rules[stride]
            new_state.append(window)


        self.state = new_state

    def print_sim_state(self):
        # this could be better
        print(''.join(self.state))

sim = Rule90(10)
sim.run()
    