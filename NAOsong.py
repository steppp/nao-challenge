from naoqi import ALProxy
import sys

def play(ip, port):
    aup = ALProxy("ALAudioPlayer", ip, port)
    aup.post.playFile('music.mp3')

if __name__ == '__main__':
    ip = "127.0.0.1"
    port = 9559

    if len(sys.argv) <= 1:
        # use default values
        pass
    elif len(sys.argv) <= 2:
        ip = sys.argv[1]
    else:
        port = int(sys.argv[2])
        ip = sys.argv[1]

    play(ip, port)
