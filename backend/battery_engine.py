from backend.feature_engineering import calculate_features
from backend.predictor import predict_soh, predict_rul
from backend.safety import check_safety
from backend.digital_twin import simulate_environment


def validate_inputs(v_start, v_end, t_start, t_max, current, time, ambient_temp):
    
    if v_start <= 0 or v_end <= 0:
        return "Voltage must be positive."
    
    if time <= 0:
        return "Time must be greater than zero."
    
    if current < 0:
        return "Current cannot be negative."
    
    if t_max < t_start:
        return "Max temperature cannot be less than start temperature."
    
    if ambient_temp < -50 or ambient_temp > 100:
        return "Ambient temperature seems unrealistic."
    
    return None


def grade_battery(soh):
    if soh > 80:
        return "GRADE A"
    elif soh > 60:
        return "GRADE B"
    else:
        return "GRADE C"


def analyze_battery(v_start, v_end, t_start, t_max, current, time, ambient_temp):
    
    try:
        # Step 1: Validate inputs
        error = validate_inputs(v_start, v_end, t_start, t_max, current, time, ambient_temp)
        
        if error:
            return {
                "status": "error",
                "message": error
            }
        
        # Step 2: Feature calculation
        features = calculate_features(v_start, v_end, t_start, t_max, current, time)
        
        # Step 3: Model predictions
        soh = predict_soh(features)
        rul = predict_rul(features)
        
        # Step 4: Safety check
        temp_rise_rate = (t_max - t_start) / time
        safety_status = check_safety(temp_rise_rate)
        
        # Step 5: Digital twin simulation
        adjusted_rul = simulate_environment(rul, ambient_temp)
        
        # Step 6: Grading
        grade = grade_battery(soh)
        
        return {
            "status": "success",
            "data": {
                "state_of_health_percent": round(soh, 2),
                "base_remaining_cycles": rul,
                "adjusted_remaining_cycles": adjusted_rul,
                "safety_status": safety_status,
                "battery_grade": grade
            }
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }