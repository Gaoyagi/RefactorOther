# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Cooking:
    def __init__(self, time, temperature, pressure, state):
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.desired_state = state

    def is_cookeding_criteria_satisfied(self):
        return self.is_well_done() or self.is_medium()


    def is_well_done(self):    
        return desired_state == 'well-done' and  \
            self.get_cooking_progress() >= WELL_DONE


    def is_medium(self):
        return desired_state == 'medium' and  \
            self.get_cooking_progress() >= MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temperature * self.pressure * COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'

if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
    print('cooking is done.')
else:
    print('ongoing cooking.')