class User(object):
    
    def __init__(self, username):
        self.username = username
        self.role = 'user'

    def send_message(self, message):
        print(f'A message: {message}')

    def __str__(self):
        return f'{self.username} - {self.role}'


class Moderator(User):

    def __init__(self, username):
        self.username = username
        self.role = 'moderator'

    def ban_user(self, user, cause):
        print(f'Banned a {user}. Cause: {cause}')


class Admin(Moderator):

    def __init__(self, username):
        self.username = username
        self.role = 'admin'

    def ban_moderator(self, moderator, cause):
        print(f'Banned a {moderator}. Cause: {cause}')


alan = User('Alan22')
alan.send_message('Hello!')

moder = Moderator('Veocn3')
moder.ban_user(alan, 'Flood and spam')

admin1 = Admin('coolDude')
admin1.ban_moderator(moder, 'Ban without warning')
