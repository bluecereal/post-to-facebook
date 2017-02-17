import facebook

#Generate your access token using https://developers.facebook.com/tools/explorer,
#then copy paste it during the input request
access_token = raw_input()

graph = facebook.GraphAPI(access_token)
user = graph.get_object("me")
friends = graph.get_connections(user["id"], "friends")

print(friends)
