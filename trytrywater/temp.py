# %%
def angle2dutyus(angle):
    servo_max_degree = 180
    return (angle + servo_max_degree) * (2500 - 500) / (2 * servo_max_degree) + 500
