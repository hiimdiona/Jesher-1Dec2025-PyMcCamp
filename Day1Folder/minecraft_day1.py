# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def come():
    agent.teleport_to_player()
player.on_chat("come",come)
def move_forward(steps):
    agent.move(FORWARD,steps)

player.on_chat("mf1",move_forward)

def turn_left():
    agent.turn(TurnDirection.LEFT)

player.on_chat("tl1",turn_left)

def move_backward(steps):
    agent.move(BACKWARD,steps)
    player.on_chat("mb1",move_backward)

def turn_right():
    agent.turn(TurnDirection.RIGHT)

player.on_chat("tr1",turn_right)

def move_up(steps):
    agent.move(UP,steps)
player.on_chat("mu1",move_up)

def move_down(steps):
    agent.move(DOWN,steps)
player.on_chat("md1",move_down)


def obby1():
    agent.move(FORWARD,4)
    agent.turn(LEFT)
    agent.move(FORWARD,5)
    agent.turn(RIGHT)
    agent.move(FORWARD,3)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,3)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
player.on_chat("obby1",obby1)

################## On Chat Commands Section #####################
