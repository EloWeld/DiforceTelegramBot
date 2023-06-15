from loguru import logger
from appSchedule import ALLOWED_USER_GROUPS
from services.oneService import OneService
from utils import format_phone_number, is_in_group_hierarchy


def test_diforce_users_sync():
    users = OneService.getUsers()
    user_groups = OneService.getUsersGroups()
    filtered_users = []
    excluded_user_groups = set()
    # Change users objects
    for x_user in users:
        if x_user['Phone']:
            x_user['Phone'] = format_phone_number(x_user['Phone'])
        if is_in_group_hierarchy(x_user['GroupID'], ALLOWED_USER_GROUPS, user_groups):
            filtered_users.append(x_user)
        else:
            g = [x for x in user_groups if x['GroupID'] == x_user['GroupID']]
            excluded_user_groups.add(g[0]['GroupName'] if g else '???')
            
    logger.info(excluded_user_groups)
    print(filtered_users)
    