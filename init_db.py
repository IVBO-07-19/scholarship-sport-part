name = input('DB name: ')
user = input('Username: ')
password = input('User password: ')

with open('djangoProject/.env', 'w') as env:
    env.write(f'DATABASE_URL = postgres://{user}:{password}@localhost:5432/{name}')