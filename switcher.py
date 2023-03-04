import jarvis_functions

def simple_switcher(query):

    match query:
        case "what time is it" | "time":
            jarvis_functions.time()

        case "what date is it today" | "date":
            jarvis_functions.date()

        case "open Firefox" | "Google" | "google" | "gg":
            jarvis_functions.Firefox()

        case "open YouTube" | "YouTube" | "youtube" | "yt":
            jarvis_functions.Youtube()

        case _:
            complex_switcher(query)


def complex_switcher(query):

    criterion = query

    if(query.find("search") == 0):
        query = query[7:]
        criterion = "search"

    if(query.find("mess to") == 0):
        query = query[8:]
        criterion = "mess"

    # if(query.find("call") == 0):
    #     query = query[5:]
    #     criterion = "call"

    match criterion:
        case "search":
            jarvis_functions.websearch(query)

        case "mess":
            jarvis_functions.WappMessage(query)
        
        # case "call":
        #     jarvis_functions.WappCall(query)

        case _:
            print("No such command")
