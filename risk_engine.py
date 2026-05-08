def calculate_risk(action, time):
    
    hour = int(time.split(":")[0])
    
    if action == "failed_login":
        return "Medium Risk"
    
    elif action == "upload":
        return "High Risk"
    
    elif hour < 5 or hour > 22:
        return "Suspicious Timing"
    
    else:
        return "Low Risk"