from qbittorrent import Client
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--addr", metavar='ADDRESS', type=str, help='qbittorrent address')
parser.add_argument("--uname", metavar='USERNAME', type=str, help='qbittorrent username', default="admin")
parser.add_argument("--passwd", metavar='PASSWORD', type=str, help='qbittorrent password', default="admin")
parser.add_argument("--port", metavar='PORT', type=str, help='qbittorrent poer', default="8080")
args = parser.parse_args()

addr = args.addr
uname = args.uname
passwd = args.passwd
port = args.port

if addr == "" or passwd == "":
    print("missing info! addr = {}, passwd= {}".format(addr, passwd))

qb = Client(f'http://{addr}:{port}/')
qb.login(uname, passwd)

torrents = qb.torrents(category='expendable')

for torrent in torrents:
    if torrent["progress"] == 1:
        if not "paused" in torrent["state"]:
            print("Pausing "+torrent["name"])
            qb.pause(torrent["hash"])
    else:
        print("{} is still downloading, at {}%".format(torrent["name"], round(float(torrent["progress"])*100) ))