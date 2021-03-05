# by Kami Bigdely
# Extract class
class Actors:
    def __init__(self, first, last, birth, email, movies=[]):
        self.first_name = first
        self.last_name = last
        self.birth_year = birth
        self.email = email
        self.movies = movies

    def send_hiring_email(self):
        print("email sent to: ", self.email)

first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']


    
for i, value in enumerate(emails):
    actor = Actors(first_names[i], last_names[i], birth_year[i], emails[i], movies[i])
    if birth_year[i] > 1985:
        print(first_names[i], last_names[i])
        print('Movies Played: ', end='')
        for m in movies[i]:
            print(m, end=', ')
        print()
        actor.send_hiring_email()