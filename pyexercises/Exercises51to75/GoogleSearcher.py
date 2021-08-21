# Create a script that let the user type in a search term and opens a search on the browser for that term on google

import webbrowser


query = input("Input your query: ")
webbrowser.open("https://google.com/search?q={}".format(query))
