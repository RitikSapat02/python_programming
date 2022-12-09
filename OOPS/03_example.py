class remote:
    pass


class player:
    def movRight(self):
        pass
    def movLeft(self):
        pass
    def movTop(self):
        pass

player1 = player()
remote1 = remote()

if(remote1.isLeftPressed()):
    player1.moveLeft()