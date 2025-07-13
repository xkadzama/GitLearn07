def reg_user():
    if login and password:
        print('Аккаунт создан')


def redirect():
    if status == True:
        return 'main.html'