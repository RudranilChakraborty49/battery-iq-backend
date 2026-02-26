def simulate_environment(base_rul, ambient_temp):
    
    if ambient_temp <= 25:
        adjustment = 1.0
    elif ambient_temp <= 35:
        adjustment = 0.85
    elif ambient_temp <= 45:
        adjustment = 0.6
    else:
        adjustment = 0.4
    
    return int(base_rul * adjustment)