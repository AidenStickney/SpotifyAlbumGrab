import spotipy
import spotipy.oauth2
from colorthief import ColorThief
import requests
import time
import pigpio
pi = pigpio.pi()


# export SPOTIPY_CLIENT_ID = "ab77ce1a99b54dfd8bae71d21d635ea4"
# export SPOTIPY_CLIENT_SECRET = "f8fd7485778245f3a27c3a5d32e1641f"
# export SPOTIPY_REDIRECT_URI = "https://www.google.com"

# # Get the username from terminal
# username = sys.argv[1]
# scope = 'user-read-private user-read-playback-state user-modify-playback-state'

# # Erase Cache and ask permission
# try:
#     token = util.prompt_for_user_token(username, scope)
# except (AttributeError, JSONDecodeError):
#     os.remove(f".cache-{username}")
#     token = util.prompt_for_user_token(username, scope)
    
# # Create Spotify object
# spotifyObject = spotipy.Spotify(auth=token)

# sp = spotipy.Spotify(str(token))

# token = str(input('Enter token: '))

token = 'BQCQnTDDXJebkKNZFuXAwrDFJsGi18rTQdJUq5WPBuZw5AMBfXNdbFaZEmiijBlLmmxIp4-WMIADd14A72c9ruBG3MC6pQwvhvW89fGZv7Mvs3qSZ7MnSTl_M_O501wJaWmfUGNKgfA2oLxU_6pbEI33CgshE--oa_0-E6wQAJMS2w'

sp = spotipy.Spotify(token)

past_playback = 0

while True:
    
    current_playback = sp.current_playback()
    if current_playback != None:
        current_playback = sp.current_playback()
        
        if current_playback['item']['uri'] != past_playback:
            past_playback = current_playback['item']['uri']
            
            # Get info on song
            duration = current_playback['item']['duration_ms']
            album_artwork = current_playback['item']['album']['images'][0]['url']
            
            # Find Dominant colors
            print('Finding Colors')
            image = ColorThief(requests.get(album_artwork, stream=True).raw)
            # palette = image.get_palette(quality=1)
            # sns.palplot([tuple(i / 255 for i in j) for j in palette])
            
            # Bar Image
            # palette = (np.array(palette)).astype(np.uint8)
            
            rms_lst = []
            
            # for img_clr, img_hex in webcolors.CSS3_NAMES_TO_HEX.items():
            #     cur_clr = webcolors.hex_to_rgb(img_hex)
            
            # for color in palette:
            #     rmse = np.sqrt(mean_squared_error(color, cur_clr))
            #     rms_lst.append(rmse)
            #     closest_color = rms_lst.index(min(rms_lst))
            #     nm = list(webcolors.CSS3_NAMES_TO_HEX.items())[closest_color][0]
                # print(nm)
            
            # title = "p"
            # #creating bar image
            # cols = len(palette)
            # rows = max([1,int(cols/2.5)])
            
            # Create color Array
            # barFullData = np.tile(palette, (rows,1)).reshape(rows, cols, 3)
            
            
            # Create Image from Array
            # barImg = Image.fromarray(barFullData, 'RGB')
            
            #saving image
            # barImg.save("{}_{}.png".format(title,"method"))
            # barImg.show()
            
            
            dom_color = image.get_color(quality=1)
            # print(dom_color)
            # rmse = np.sqrt(mean_squared_error(dom_color, cur_clr))
            # rms_lst.append(rmse)
            # closest_color = rms_lst.index(min(rms_lst))
            # nm = list(webcolors.CSS3_NAMES_TO_HEX.items())[closest_color][0]
            # print(nm)
            
            print('Changing Colors')
            pi.set_PWM_dutycycle(17, dom_color[0])
            pi.set_PWM_dutycycle(22, dom_color[1])
            pi.set_PWM_dutycycle(24, dom_color[2])
            
            print('Sleeping for 3 secs.')
            time.sleep(3)
    else:
        print("Nothing Currently Playing")
        
        time.sleep(3)

    # image = ColorThief(requests.get(album_artwork, stream=True).raw)
    # dominant_color = image.get_color(quality=1)




# SPOTIFY_GET_CURRENT_TRACK_URL = ''
# SPOTIFY_ACCESS_TOKEN = ''

# def get_current_track(access_token):
#     response = requests.get(
#         SPOTIFY_GET_CURRENT_TRACK_URL,
#         headers={
#             "Authorization": f"Bearer {access_token}"
#         }
#     )
#     resp_json = response.json()
    
#     track_id = resp_json['item']['id']
#     track_name = resp_json['item']['id']
    
#     current_track_info = {
#         "id": track_id,
#         "name": track_name,
#         "artists": artist_name,
#         "link": link
#     }
    
#     return current_track_info
    

# def main():
#     current_track_info = get_current_track(
#             SPOTIFY_ACCESS_TOKEN
#     )
    
#     pprint(current_track_info, indent=4)








# sp = spotipy.Spotify(auth_manager=auth_manager)


# track_info = sp.track()