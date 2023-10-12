
from ds_protocol import join, post, bioo, errorHandling
import socket

# NAME Andrew Z. Ho
# EMAIL andrewzh@uci.edu
# STUDENT ID 11211101

### IP Address: 168.235.86.101
### Port: 3021

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  test = errorHandling(server, port, username, password, message, bio)
  if test:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))
    conditions = False
    try:
      x = join(username, password, sock)
      print(x["response"]["message"])
      tp = x["response"]["type"]
      token = x["response"]["token"]
      conditions = True
    except:
      return False

    if conditions:
      if tp == "ok":
        if message.isspace() == False:
          if message != "":
            try:
              y = post(message, sock, token)
              print(y["response"]["message"])
            except:
              print('uhoh there was an error!!')
              return False
          else:
            pass
        else:
          pass


        if bio == None:
          return True
        else:
          if bio.isspace() == False:
            if bio != "":
              try:
                z = bioo(bio, sock, token)
                print(z["response"]["message"])
                return True
              except:
                pass
            else:
              pass
          else:
            pass
  else:
    print("Error with input!!")
  #TODO: return either True or False depending on results of required operation

if __name__ == "__main__":
  send('168.235.86.101', 3021, "kirby", '123', 'oooweee', ' ')
  ### IP Address: 168.235.86.101
  ### Port: 3021