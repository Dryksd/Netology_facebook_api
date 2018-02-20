import facebook     # pip install facebook-sdk

graph = facebook.GraphAPI(access_token='')      #https://developers.facebook.com/tools/access_token/
profile = graph.get_object("me")
friends = graph.get_connections(id="me", connection_name="friends")
friend_list = [friend["name"] for friend in friends["data"]]

print(friend_list, friends)

