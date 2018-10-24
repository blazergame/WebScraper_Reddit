# Introduction
# Running this script will take 2 mandatory parameters
#        argv[1] = string you want to search on
#        argv[2] = subreddit you want to search in
# 
# To run it, you'll need to have python 3 installed.
# Once installed, run the index file
# Ex: py index.py tendies wallstreetbets
#
# First parameter is tendies (aka the string I want to search on)
# Second parameter is subreddit (wallstreetbets is /r/wallstreetbets)
# 
### IMPORTANT ###
# It is case SENSITIVE 
# Ex: 'tendies' is different than 'Tendies'
#   : 'John' is different than 'JOHN' or 'john'


import sys
from psaw import PushshiftAPI

print ('\n ============================================================= \n')
print ('\n ================     REDDIT WEBSCRAPPER      ================ \n')
print ('\n ============================================================= \n')

# Instantiate API wrapper
api = PushshiftAPI()

print ('\n Currently searching... \n')

# Search for given string
gen = api.search_comments(q=sys.argv[1], subreddit=sys.argv[2])

# Max amount of time in milliseconds that the query will search
# Remove number if you want to search everything within a subreddit (Note: This will take forever. Literally)
max_response_cache = 3000  # 3 seconds
cache = []

for c in gen:
    cache.append(c)

    # Remove the following two lines of code if you're not going to limit the search time(if you remove max_resposne_cache)
    if len(cache) >= max_response_cache:
        break

# Find occurance of given word
occurence = len(cache)

# Print the count
print ('Number of occurences for {} is: {}'.format(sys.argv[1], occurence) )

