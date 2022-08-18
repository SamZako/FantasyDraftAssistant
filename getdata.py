import os

def adp():
    draftShark = getDraftSharkAdp()

def getDraftSharkAdp():
    os.system('curl "https://www.draftsharks.com/adp/ppr?AdpForm%5BorderField%5D=ffnOverall&AdpForm%5BorderDirection%5D=4&AdpForm%5BleagueSize%5D=12&AdpForm%5BleagueSize%5D=8" -o tmp.txt')
    playerList = []
    with open('tmp.txt') as f:
        lines = f.readlines()
    for line in lines:
        if ('<tr data-key="' in line):
            playerList.append(line)
    tmp = playerList
    playerList = []
    for player in tmp:


    return playerList
