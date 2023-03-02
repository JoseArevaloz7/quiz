def checkUser(data, user):
    for index, item in data:
        if item['user'] == user:
            return [True, index]
    return False


def checkPass(data, _pass, user):
    for index, item in enumerate(data):
        if item['pass'] == _pass and item['user'] == user:
            return [True, index]
    return [False, -1]

