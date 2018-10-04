import datetime
import fb_auth
import tinder_api
import os
import getpass

clear = lambda: os.system('cls')
fb_username = raw_input("Username/Email: ")
fb_password = getpass.getpass(prompt='Password: ', stream=None) 
if fb_username != None and fb_password != None:
    print "Start: " + str(datetime.datetime.now())
    f = open("countFile.txt", "r")
    if os.stat("countFile.txt").st_size == 0 : 
        count = 0
    else:
        count = int(f.readline()) + 1
    f = open("countFile.txt", "w+")
    myLoves = open("myLoves.txt", "a")
    tinder_api.fb_access_token = fb_auth.get_fb_access_token(fb_username, fb_password)
    tinder_api.fb_user_id = fb_auth.get_fb_id(tinder_api.fb_access_token)
    tinder_api.authverif()
    didIFindMyLove = False
    totalFound = 0
    totalFoundInfo = ''
    try:
        while didIFindMyLove == False:
            person = tinder_api.get_person(count)
            distance_km = 0
            if 'gender' in person:
                try:
                    distance_mi = float(person['distance_mi'])
                except:
                    distance_mi = 0
                distance_km = float(distance_mi) * 1.609344
                if int(person['gender']) == 1 and int(distance_km) < 100:
                    detail = "ID: " + str(count) + " Img: " + str(person['photos'][0]['url']) + " Distance: " + str(distance_km) + " km"
                    totalFound += 1
                    myLoves.writelines(detail + ' \n')
                    totalFoundInfo =" Total Found: " + str(totalFound) + " Detail: " + detail
            clear()
            print "Current ID: " + str(count) + " Distance : " + str(distance_km)  + " km " + totalFoundInfo
            count += 1
    except:
        f.truncate()
        f.writelines(str(count))
        f.close()
        myLoves.close()
print "End: " + str(datetime.datetime.now())