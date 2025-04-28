users:list=(
    {"name":"Zosia", "location":"Poznań","posts":400},
    {"name":"Monika", "location":"Nowy_Sącz","posts":500},
    {"name":"Julka", "location":"Rzeszów","posts":700},
    {"name":"Beata", "location":"Lublin","posts":200},
)



def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów")

get_user_info(users)