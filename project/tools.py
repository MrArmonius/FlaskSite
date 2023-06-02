from flask_login import login_required, current_user

def check_user_owned_uuid(orm):
	# Check if the uuid is owned by the correct user
	user_log = int(current_user.get_id())
	user_uuid = orm.userId
	if(user_log != user_uuid):
		return False
	else:
		return True