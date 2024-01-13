import requests

class WhoID:
    def __init__(self, token):
        self.token: str = token

    def check_user(self, mail, password):
        try:
            response = requests.get(
                f'https://whoid.ru/api/get?token={self.token}&mail={mail}&password={password}'
            ).json()
            return response
        except Exception as e:
            return e

    def check_fio(self, fio):
        try:
            response = requests.get(
                f'https://whoid.ru/api/fio?token={self.token}&name={fio}'
            ).json()
            return response
        except Exception as e:
            return e



if __name__ == "__main__":
    finder = WhoID('0dbda7b1-a64e-4927-940d-e8837cd25e83')
    user = finder.check_user('ser@mail.ru', 'abc123')
    fio = finder.check_fio('Сергеев Сергей')
    print(user)
    print(fio)