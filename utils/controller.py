def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów")

def add_user(users_data:list)->None:
    new_name=input('podaj imię nowego użytkownika: ')
    new_location=input('podaj lokalizację: ')
    new_posts=int(input('podaj liczbę postów: '))
    users_data.append({"name" :new_name , "location": new_location ,"posts": new_posts},)

def remove_user(users_data:list)->None:
    użytkownik_do_usunięcia = input('podaj użytkownika: ')

    for user in users_data:
        if user['name'] == użytkownik_do_usunięcia:
            users_data.remove(user)

def update_user(users_data:list)->None:
    użytkownik_do_edycji = input ('podaj uzytkownika do edycji: ')
    for user in users_data:
        if user['name'] == użytkownik_do_edycji:
            user['name']=input('podaj nowe imię użytkownika: ')
            user['location']=input('podaj nową lokalizację: ')
            user['posts']=int(input('podaj nową ilość postów: '))