current_user = ['admin','jack','mike','tom','hack']
new_users = ['admin','hack','jerry','lucy','red']
for new_user_0 in new_users:
    if new_user_0 not in current_user:
        print(f"{new_user_0} is available.")
    else:
        print(f"{new_user_0} is not available.")
