from api.service.strongify_service import strongify_password

print("", strongify_password(password="batadaca", target_size=8))
print("", strongify_password(password="bat0At12f", target_size=8))
print("", strongify_password(password="a", target_size=4))
print("", strongify_password(password="pimpolh0!", target_size=8))
