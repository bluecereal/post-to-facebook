import facebook

access_token = raw_input()

graph = facebook.GraphAPI(access_token)
user = graph.get_object("me")
friends = graph.get_connections(user["id"], "friends")

print(friends)
