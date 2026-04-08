def get_legit_power_users(log_data, bot_ids, threshold):
    user_action = {}
    for timestamp, user_id, action_type in log_data:
        if user_id in bot_ids:
            continue
        if user_id not in user_action:
            user_action[user_id] = set()
        user_action[user_id].add(action_type)
    powerusers = []
    for user_id, unique_actions in user_action.items():
        if len(unique_actions) > threshold:
            powerusers.append(user_id)

    return sorted(powerusers)

log_data = {
    ("10:01", "u1", "view"), 
    ("10:02", "u2", "view"), 
    ("10:05", "u1", "scroll"), 
    ("10:10", "u1", "view"), 
    ("10:12", "u9", "extract")
}
bot_ids = {"u9"}
threshold = 1
print(get_legit_power_users(log_data, bot_ids, threshold))



















