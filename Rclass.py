class Pctr:
    def __init__(self,tank, cs_l, cs_r):
        self.tank = tank
        self.cs_l = cs_l
        self.cs_r = cs_r
    def run(self, speed, p_gain):
        reflected_light_l = self.cs_l.reflected_light_intensity
        reflected_light_r = self.cs_r.reflected_light_intensity

        tank_steering = (reflected_light_l - reflected_light_r) * self.p_gain

        self.tank.on(tank_steering, speed, p_gain)