import requests, base64, gzip, itertools, hashlib, random, time

username = "iusearchbtw"
password = "arch-btw99"
accountID = "23725858"
levelString = "H4sIAAAAAAAAC6WOwWoDMQxEf0hbPJLltVl6SHopvS6B9iRCAqHNL_TjK1uF9pAQQgzW2PLMs86rVIIlY9_iGzBWNXCIDMk2wYohpWSzwaC9VLdXw_cdcTwWbxfj3ROB8N-AsPX8JRD4D3RzFr2KSfdMU65g6LyBUOqiISUkk9c4z9H5ldpllTZuPGoAxsMmE7zGK1IIKC0gFDAxTdxI_KIkheD9luBtrvqvTep-73meO8tJzRdJJ7qTSWuEfVAmyT08K-nsMWHCU3YzaL9uceDd6eP97Wv_sv08vh6el4EmltbGn5N_uvwAZJh_AKECAAA="

# You can upload only 5 levels an hour, decreasing this gets you ratelimited for a while. Python Requests is very slow so you shouldnt have issues.
# Verified by Kitsune YouTuber nerd himself
# https://www.reddit.com/r/geometrydash/comments/14x9icw/comment/jrmxe2j/

def xor_cipher(string, key):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(string, itertools.cycle(key)))

def generate_chk(values=[], key="", salt=""):
    values.append(salt)
    string = "".join(map(str, values))
    hashed = hashlib.sha1(string.encode()).hexdigest()
    xored = xor_cipher(hashed, key)
    return base64.urlsafe_b64encode(xored.encode()).decode()

def generate_upload_seed(data, chars=50):
    if len(data) < chars:
        return data
    step = len(data) // chars
    return data[::step][:chars]

def encode_level(level_string, is_official_level):
    gzipped = gzip.compress(level_string.encode())
    base64_encoded = base64.urlsafe_b64encode(gzipped)
    if is_official_level:
        base64_encoded = base64_encoded[13:]
    return base64_encoded.decode()

def gjp_encrypt(data):
    return base64.b64encode(xor_cipher(data, "37526").encode()).decode()

while True:
    req = requests.post("http://www.boomlings.com/database/uploadGJLevel21.php", data={"gameVersion": 21,"accountID": accountID, "gjp": gjp_encrypt(password), "userName": username, "levelID": 0,"levelName": f"i use arch btw {str(random.randint(1,10000))}", "levelDesc": "","levelVersion": 1,"levelLength": 0,"audioTrack": 0,"auto": 0,"password": 0,"original": 0,"twoPlayer": 0,"songID": 1,"objects": 0,"coins": 0,"requestedStars": 0, "unlisted": 0,"ldm": 0,"levelString": encode_level(levelString, False), "seed2": generate_chk(key="41274", values=[generate_upload_seed(levelString)], salt="xI25fpAapCQg"), "secret": "Wmfd2893gb7"}, headers={"User-Agent":""}).text
    if req == "-1":
        print("Failure due to either invalid login, creator banned or skill issue.")
    elif:
        print("Success!")
    time.sleep(720)
