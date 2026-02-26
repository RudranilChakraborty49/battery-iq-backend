from backend_service import process_battery_input

# This simulates what frontend will send
input_data = {
    "v_start": 4.2,
    "v_end": 3.8,
    "t_start": 25,
    "t_max": 35,
    "current": 2.0,
    "time": 10,
    "ambient_temp": 40
}

result = process_battery_input(input_data)

if result["status"] == "error":
    print("Error:", result["message"])
else:
    data = result["data"]
    
    print("\n🔋 Battery Analysis Report")
    print("----------------------------")
    print("State of Health:", data["state_of_health_percent"], "%")
    print("Base Remaining Life:", data["base_remaining_cycles"], "cycles")
    print("Adjusted Remaining Life:", data["adjusted_remaining_cycles"], "cycles")
    print("Safety Status:", data["safety_status"])
    print("Grade:", data["battery_grade"])