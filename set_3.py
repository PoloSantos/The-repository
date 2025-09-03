'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "set_3_sample_data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    fromlist = list(social_graph[from_member]["following"])
    tolist = list(social_graph[to_member]["following"])
    x = False
    y = False
    
    for name in fromlist:
        if name == to_member:
            x = True

    for name in tolist:
        if name == from_member:
            y = True

    if x == True and y == True:
        status = "friends"
    else:
        if x == True:
            status = "follower"
        if y == True:
            status = "followed by"
        if x == False and y == False: 
            status = "no relationship"

    print(status)
    return status


relationship_status("@chums","@joaquin",social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
    })


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "set_3_sample_data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #Xwinner
    #Owinner
    winner = "NO WINNER"

    bl = [0,0,0,0,0,0]
    lol = len(board) - 1
    gl = [lol,lol,lol,lol,lol,lol]
    x = 0
    while x < len(board):
        bl[x] = x
        x += 1
    x = 0
    y = lol
    while x < len(board):
        gl[x] = y
        x += 1
        y -= 1

    for row in board:
        if row[bl[0]] == row[bl[1]] == row[bl[2]] == row[bl[3]] == row[bl[4]] == row[bl[5]]:
            if row[0] == "X":
                winner = "X"
            if row[0] == "O":
                winner = "O"
    y = 0
    while y < len(board):
        if board[bl[0]][y] == board[bl[1]][y] == board[bl[2]][y] == board[bl[3]][y] == board[bl[4]][y] == board[bl[5]][y]:
            if board[0][y] == "X":
                winner = "X"
            if board[0][y] == "O":
                winner = "O"
        y += 1
        
    if board[bl[0]][bl[0]] == board[bl[1]][bl[1]] == board[bl[2]][bl[2]] == board[bl[3]][bl[3]] == board[bl[4]][bl[4]] == board[bl[5]][bl[5]]:
            if board[0][0] == "X":
                winner = "X"
            if board[0][0] == "O":
                winner = "O"

    if board[bl[0]][gl[0]] == board[bl[1]][gl[1]] == board[bl[2]][gl[2]] == board[bl[3]][gl[3]] == board[bl[4]][gl[4]] == board[bl[5]][gl[5]]:
            if board[0][gl[0]] == "X":
                winner = "X"
            if board[0][gl[0]] == "O":
                winner = "O"  

    return winner

board1 = [
['O','','X'],
['X','X','O'],
['X','O','O'],
]

tic_tac_toe(board1)

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "set_3_sample_data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    keyz = list(route_map.keys())
    final = 0
    i = 0
    j = 0
    h = 0
    if route_map.get((first_stop,second_stop), False) != False:
        final = route_map[(first_stop,second_stop)]["travel_time_mins"]
    else:
        while j == 0:
            i = i%(len(keyz))
            if keyz[i][0] == first_stop:
                final = final + route_map[keyz[i]]["travel_time_mins"]
                i += 1
                h = 1
                     
            else:
                if keyz[i][1] == second_stop and h == 1:
                        final = final + route_map[keyz[i]]["travel_time_mins"]
                        j = 1
                if h == 1 and j == 0:
                    final = final + route_map[keyz[i]]["travel_time_mins"]
                    i += 1
                else: 
                    i += 1
            
    return final

legs1 = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}
eta("admu","admu",legs1)