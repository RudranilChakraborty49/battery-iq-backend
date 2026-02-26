import numpy as np

def calculate_features(v_start, v_end, t_start, t_max, current, time):
    
    if time == 0:
        raise ValueError("Time cannot be zero.")
    
    voltage_drop_rate = (v_start - v_end) / time
    temp_rise_rate = (t_max - t_start) / time
    
    if current == 0:
        internal_resistance = 0
    else:
        internal_resistance = (v_start - v_end) / current
    
    avg_current = current
    
    return np.array([[voltage_drop_rate,
                      temp_rise_rate,
                      internal_resistance,
                      avg_current]])