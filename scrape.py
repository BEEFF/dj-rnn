
import time
import sys
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

LIMIT = 100
DEPTH = 500

client_credentials_manager = SpotifyClientCredentials(client_id='a345a7b145164b0ca2d9db0b320b533d', client_secret='db220f89950449119ed71ece4682b2be')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None

def show_recommendations_for_artist(artist, artists):
    albums = []
    try:
        results = sp.recommendations(seed_artists = [artist['id']], limit=LIMIT)
    except:
        results = []
    if not results:
        return None
    for track in results['tracks']:
        selecta = track['artists'][0]['name']
        artists.append(selecta)
    return artists

def recurse(artist, depth=DEPTH, new_set=set([]), already=set([])):
    limit = 10
    count = 0
    artists = show_recommendations_for_artist(artist, [])
    if artists:
        for a in artists:
            #print("Getting artists related to {0}".format(a))
            if a not in new_set:
                recs = show_recommendations_for_artist(get_artist(a), [])
                if recs:
                    art_set = set(recs)
                    new_set = new_set | (art_set)

    if depth == 0:
         return new_set
    else:
        depth = depth -1
        try:
            artist = random.choice(list(new_set- already))
        except:
            return new_set
        already = set([artist]) | already
        return new_set | recurse(artist, depth, new_set, already)

def relate_multi(artists):
    print(artists)
    data = set([])
    for a in artists:
        print(a)
        data = data | relate(get_artist(a))
    return data

def relate(artist):
    best = set([])
    for i in range(1,5):
         data = recurse(artist)
         if len(data) > len(best):
             best = data
    return best

def to_file(data, filename):
    with open('dnb.csv', 'w') as f:
        for item in data:
            f.write("%s\n" % str.lower(item))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(('Usage: {0} artist name'.format(sys.argv[0])))
    else:
        names = sys.argv[1:]
        #artist = get_artist(name)
        #if artist:
        data = relate_multi(names)
        print(data)
        print(len(data))
        to_file(data, "{0}.csv".format(names[0]))
       # else:
         #   print("Can't find that artist", name)
