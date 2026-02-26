from backend.battery_engine import analyze_battery

def process_battery_input(input_data):
    """
    input_data should be a dictionary containing:
    v_start, v_end, t_start, t_max, current, time, ambient_temp
    """
    
    return analyze_battery(
        v_start=input_data["v_start"],
        v_end=input_data["v_end"],
        t_start=input_data["t_start"],
        t_max=input_data["t_max"],
        current=input_data["current"],
        time=input_data["time"],
        ambient_temp=input_data["ambient_temp"]
    )