import pandas as pd
from dijkstar import Graph, find_path
import json


# graph.add_edge(1,2,22)
# graph.add_edge(2,3,11)
# graph.dump(r'C:\Users\Omer\Documents\Python\stock scanner')

def load_users():
    with open(r'C:\Users\Omer\Documents\Python\stock scanner\Users.json') as f:
        data = json.load(f)
    return data

def get_id_of_genre():
    dict = {}
    for row in range(0,1937):
        dict[df.iloc[row,0]] = row
    return dict
        
def create_graph():
    for row in range(0,1937):
        for col in range(1,1937):
            weight=int(df.iloc[row,col])
            if(weight == 0):
                continue
            else:
                graph.add_edge(row,col,1/weight)
        if(row%500 == 0):print(row)

def find_match(username,list_of_users,genres_id):
    users = dict(list_of_users['Users'])
    target_user_genres = users[username]
    for name,genre in users.items():
        if(name != username):       #skip the target username
            for target_genres in range(0,len(target_user_genres)):
                for user_genres in range(0,len(genre)):
                    target = genres_id[target_user_genres[target_genres]]
                    user = genres_id[genre[user_genres]]
                    print('-----------------------------------------------------')
                    print(username,' To ',name,'Genre: ',target_user_genres[target_genres],'-->',genre[user_genres])
                    print(find_path(graph,target,user))


df = pd.read_csv (r'C:\Users\Omer\Documents\Python\stock scanner\network_matrix_final.csv')
graph = Graph()

create_graph()
find_match('User1',load_users(),get_id_of_genre())
# gener_id_dict = get_id_of_genre()


# for row in range(0,1937):
#     for col in range(0,1937):
#         print('------------------------------------------------')
#         try:
#             print(find_path(graph, row, col))
#         except Exception as e:
#             print(e)


# import json
# with open('C:\Users\Omer\Documents\Python\stock scanner\Users.json') as f:
#     data = json.load(f)

# print(data)


# len_of_user = len(data['Users']['User1'])

# for gener in range(0,len_of_user):
#     print(gener)
