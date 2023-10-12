# a3.py
from itertools import count
from pathlib import Path
from Profile import Profile, Post
from ds_client import send
from ui import *
from json import load
# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python
def path_validity_checker(master_list):
    location = master_list[0]
    p1 = Path('.') / location
    if p1.exists():
        return True
    else:
        return False
    pass

def checker(x):
    y = x.strip()
    if y == "":
        return False
    else:
        return True

def quote_checker(second):
    if second[0] == "\"" and second[-1] == "\"":
        section = second[1:-1]
        return section
    elif second[0] == "\'" and second[-1] == "\'":
        section = second[1:-1]
        return section
    else:
        return False

def profileCreator(x):
    po = Profile(x[0], x[1],x[2])
    if len(x) < 6:
        po.bio = None
    elif len(x) == 6:
        po.bio = x[4]
    p = Post(x[3])
    po.add_post(p)
    return x

def C(): ## creates file
    ## os. path. join(save_path, file_name)
    ## master_list == location command name
    master_list = create_files()
    print(master_list)
    list1 = ['-n']
    print('hihi')
    ## check that lsit of 1 is location 2 is -n and location 3 is a file name with no '.'
    conditions = path_validity_checker(master_list)
    if conditions:
        if master_list[1] in list1:
            print('hihi')
            if '.dsu' in master_list[2]:
                print("ERROR IN NAME")
            else:
                corrected_file = master_list[2] + ".dsu"
                x = master_list[0] ## directory
                full_name = master_list[0] + x[2] + corrected_file
                print(full_name)
                potential = [full_name]
                p1 = Path(full_name)
                if not p1.exists():
                    global loaded
                    loaded = True
                    global user1
                    print('Enter a username: ')
                    username = input()
                    one = checker(username)
                    if one:
                        if ' ' in username:
                            username = username.replace(' ', '')
                        print('Enter a password: ')
                        password = input()
                        one = checker(password)
                        if one:
                            if ' ' in password:
                                password = password.replace(' ', '')
                            print('Enter a bio: ')
                            bio = input()
                            one = checker(bio)
                            if one:
                                print('Enter a server: ')
                                dsuserver = input()
                                one = checker(dsuserver)
                                if one:
                                    p1.touch()
                                    user1 = Profile(dsuserver, username, password)
                                    user1.bio = bio
                                    user1.save_profile(full_name)
                                else:
                                    print("ERROR")
                            else:
                                print("ERROR")
                        else:
                            print("ERROR")
                elif p1.exists():
                    O(potential)
        return user1
    else:
        print('Invalid Directory')
 ## C:\users\andyh\a3test
def O(x):
    if path_validity_checker(x):    
        global loaded
        loaded = True
        global user1
        global full_name ## directory
        try:
            full_name = x[0]
            reverse = full_name[len(full_name):None:-1]
            location = reverse.index('.')
            extension = reverse[0:location]
        except:
            extension = None
        if extension == 'usd':
            bull = None
            try:
                f = open(full_name)
                data = load(f)
                keys = data.keys()
                bull = True
            except:
                bull = False
            if bull == True:
                condition = 0
                list1 = ['dsuserver', "username", "password", "bio", "_posts"]
                for i in keys:
                    if i in list1:
                        condition += 1
                
                if condition == 5 and len(keys) == 5:
                    user1 = Profile()
                    user1.load_profile(x[0])
                    print('File Loaded!')
                    return user1
                else:
                    print('ERROR')
                    return False
            else:
                print("ERROR")
                return False
        else:
            print("ERROR")
            return False
    else:
        print("ERROR")
        return False

def Edit(initial, x):
    if ' -' in initial:
        string = initial[1:len(initial)]
        final = string.split(' -')
        final.pop(0)
        list1 = ['usr', 'pwd', 'bio', 'addpost', 'delpost']
        status = None
        edits = True
        for i in final:
            try:
                y = i.index(' ')
                first = i[0:y]
                second = i[y+1:len(i)]
                status = True
            except:
                print('ERROR')
                edits = False
            if edits == True:
                quote = quote_checker(second)
                if quote == False:
                    status = False
                else:
                    second = quote
                if status == True:
                ## username
                    if first == list1[0]:
                        if ' ' in second:
                            print('ERROR')
                            edits = False
                        else:
                            x.username = second
                            x.save_profile(full_name)
                    ## password
                    if first == list1[1]:
                        if ' ' in second:
                            print('ERROR')
                            edits = False
                        else:
                            x.password = second
                            x.save_profile(full_name)
                    ## bio
                    if first == list1[2]:
                        x.bio = second
                        x.save_profile(full_name)
                    ## addpost
                    if first == list1[3]:
                        words = second
                        po = Post(words)
                        x.add_post(po) 
                        x.save_profile(full_name)
                    ## delpost
                    if first == list1[4]:
                        try:
                            int(second.strip())
                            truth = True
                        except:
                            truth = False
                        if truth == True:
                            number = second
                            try:
                                x.del_post(int(number))
                                x.save_profile(full_name)
                            except:
                                print("ERROR")
                    if first not in list1:
                        edits = False
                        print("ERROR")
                else:
                    print("ERROR: Forgot quotes")
            else:
                break
    else:
        print("ERROR")
    
def P(initial, x): ## initial can be seen as the final completed input and x is the Profile Object
    if ' -' in initial:
        string = initial[1:len(initial)]
        final = string.split(' -')
        final.pop(0)
        list1 = ['usr', 'pwd', 'bio', 'posts', 'post', 'all']
        
        for i in final:
            stripped = i.replace(" ", '')
            if stripped == i:
                ## username
                if i == list1[0]:
                    print(x.username)
                ## password
                elif i == list1[1]:
                    print(x.password)
                ## bio
                elif i == list1[2]:
                    print(x.bio)
                ## posts
                elif i == list1[3]:
                    posts = x.get_posts()
                    for i in posts:
                        if i["entry"] == '':
                            print('EMPTY')
                        else:
                            print(i["entry"])
                ## all
                elif i == list1[5]:
                    print(x.dsuserver)
                    print(x.username)
                    print(x.password)
                    print(x.bio)
                    print(posts[0]["entry"])
                    for i in posts:
                        print(i["entry"])
                else:
                    print("ERROR")
            else:
                if ' ' in i:
                    ## post
                    y = i.index(' ')
                    first = i[0:y]
                    second = i[y:len(i)]
                    truth = None
                    try:
                        int(second.strip())
                        truth = True
                    except:
                        truth = False
                    if first == list1[4] and truth == True:
                        post_id = int(second.strip())
                        posts = x.get_posts()
                        if post_id <= len(posts):
                            if posts[post_id - 1]["entry"] == '':
                                print("EMPTY")
                            else:
                                print(posts[post_id - 1]["entry"])
                        else:
                            print("ERROR")
                    else:
                        print("ERROR")
                else:
                    print("ERROR")
    else:
        print("ERROR")

def online(): ## A
    global prof
    global counts
    global ports
    if prof == None:
        x = get_info() ## the format is [server, username, password, message, bio, port] in a list
        ports = int(x[5])
        prof = profileCreator(x)
    else:
        something = get_info1()
        x = [prof[0], prof[1], prof[2]]
        for i in something:
            x.append(i)
            print(x)
            

    if len(x) <= 4:
        idk = send(x[0], ports, x[1], x[2], x[3])
    elif len(x) >= 5:
        idk = send(x[0], ports, x[1], x[2], x[3], x[4])

def uploadJournal(final): ## U
    ## [directory, number]
    truth = False
    try:
        p = O(final[0])
        truth = True
    except:
        pass
    if truth:
        truth1 = False
        try:
            int(final[1].strip())
            truth1 = True
        except:
            truth1 = False
        if truth1 == True:
            post_id = int(final[1].strip())
            posts = x.get_posts()
            if post_id <= len(posts):
                if posts[post_id - 1]["entry"] == '':
                    print("EMPTY")
                else:
                    text = posts[post_id - 1]["entry"]
                    send(p.dsuserver, port, p.username, p.password, text)
            else:
                print("ERROR post ID longer than total posts")
        else:
            print("ERROR not an Integer")

if __name__ == "__main__":
    global port 
    port = None

    global ports
    ports = None

    global loaded
    loaded = None

    global user1
    user1 = None

    global prof
    prof = None

    while True:
        x = start() ## gets what function is being run as in E P C etc.
        if x == True:
            online()
        elif x == 'C':   
            y = C()
        elif x == 'O':
            y = open_files()
            user1 = O(y)
        elif x == 'U':
            y = postJournal() ## returns as [directory post#] in a list
            uploadJournal(y)
        elif x == "E" or x == "P":
            if loaded == True:
                if x == 'E':
                    y = edit_files()
                    print(y)
                    Edit(y, user1)
                elif x == 'P':
                    y = print_files()
                    print(y, user1)
            else:
                print('FILE NOT LOADED')
        elif x == 'Q':
            break
        else:
            print("ERROR")
        

# NAME Andrew Z. Ho
# EMAIL andrewzh@uci.edu
# STUDENT ID 11211101
