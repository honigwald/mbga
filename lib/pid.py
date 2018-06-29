class PID:
    def __init__(self, target_temp):
        self.p_fact = 1.0
        self.i_fact = -0.01
        self.i_total = 0.0
        self.d_fact = -5.0
        self.last_error = None
        self.target_temp = target_temp

    def update(self, curr_temp):
        error = self.target_temp - curr_temp
        if self.last_error == None:
            self.last_error = error
        self.i_total += error
        PID = (error * self.p_fact)
        PID += ((error - self.last_error) * self.d_fact)
        PID += (self.i_total * self.i_fact)
        self.last_error = error

        return PID

'''
p_fact = 1.0
i_fact = -0.01
i_total = 0.0
d_fact = -5.0
last_e = None
while True:
  e = t_set - read_temp()
  if last_e is None:
    last_e = e
  i_total += e
  if (e * p_fact + (e - last_e) * d_fact + i_total * i_fact) > 0.0:
      heating_on(True)
  else:
      heating_on(False)
  last_e = e
  time.sleep(300.0)
'''