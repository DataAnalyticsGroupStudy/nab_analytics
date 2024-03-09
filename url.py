import requests as rq


# My api key -  
myApi = ""
headers = {"Authorization": f"{myApi}"}

def team(ID = None):
    # Originally -> GET https://api.balldontlie.io/v1/teams
    # Want to get specific team -> GET https://api.balldontlie.io/v1/teams/<ID>
    if (ID == None):
        teams = "https://api.balldontlie.io/v1/teams/"
     
    else :
        teams = "http://api.balldontlie.io/v1/teams/{}".format(ID)

    response = rq.get(teams, headers=headers)
    return response.url

def player(ID = None):
    # Originally -> GET http://api.balldontlie.io/v1/players
    # Want to get specific players -> https://api.balldontlie.io/v1/players/<ID>
        if (ID == None):
            players = "http://api.balldontlie.io/v1/players"
     
        else :
            players = "http://api.balldontlie.io/v1/players/{}".format(ID)

        response = rq.get(players, headers=headers)
        return response.url

def game(ID = None):
    # Originally -> GET http://api.balldontlie.io/v1/games
    # Want to get specific games -> https://api.balldontlie.io/v1/games/<ID>
        if (ID == None):
            game = "http://api.balldontlie.io/v1/games"

        else :
            game = "http://api.balldontlie.io/v1/games/{}".format(ID)

        response = rq.get(game, headers=headers)
        return response.url

def status():
    status = "https://api.balldontlie.io/v1/stats"
    response = rq.get(status, headers=headers)
    return response.url

def seasonAvg():
     # Can use ?season=2018&player_ids[]=1&player_ids[]=2 -> return regular season averages for player_ids 1 and 2 in 2018.
        seasonAvg = "https://api.balldontlie.io/v1/season_averages"
        response = rq.get(seasonAvg, headers=headers)
        return response.url



