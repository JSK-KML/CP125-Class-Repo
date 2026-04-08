def audit_zero_trust(baseline_set, current_log_list):
    
    current_log_set = set(current_log_list)
    authorized = baseline_set & current_log_set
    alerts = current_log_set - baseline_set
    inactive = baseline_set - current_log_set
    return (authorized, alerts, inactive)


baseline_set = {
    ( "u1", "192.168.1.1" ), 
    ( "u2", "192.168.1.5" )
}
current_log_list = {
    ( "u1", "192.168.1.1" ), 
    ( "u3", "10.0.0.99" )
}
print(audit_zero_trust(baseline_set, current_log_list))