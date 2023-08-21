# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
# REFERENCE: https://www.datacamp.com/tutorial/markov-chains-python-tutorial
# REFERENCE: https://forum.freecodecamp.org/
# REFERENCE: https://github.com/Gregory-crypto/rock-paper-scissors


import numpy as np

def player(prev_play, opponent_history=[],transition_matrix={},moves=[""],guess=[""],total_moves=[0]):
  opponent_history.append(prev_play)
  response={"R":"P","P":"S","S":"R"}
  
  
  if prev_play=="":
    prev_play=np.random.choice(["R","P","S"])
    guess[0]=np.random.choice(["R","P","S"])
    total_moves[0]=0
    transition_matrix[0]={"RRR":{"R":0,"P":0,"S":0},
                          "RRP":{"R":0,"P":0,"S":0},
                          "RRS":{"R":0,"P":0,"S":0},
                          "RPR":{"R":0,"P":0,"S":0},
                          "RPP":{"R":0,"P":0,"S":0},
                          "RPS":{"R":0,"P":0,"S":0},
                          "RSR":{"R":0,"P":0,"S":0},
                          "RSP":{"R":0,"P":0,"S":0},
                          "RSS":{"R":0,"P":0,"S":0},

                          "PRR":{"R":0,"P":0,"S":0},
                          "PRP":{"R":0,"P":0,"S":0},
                          "PRS":{"R":0,"P":0,"S":0},
                          "PPR":{"R":0,"P":0,"S":0},
                          "PPP":{"R":0,"P":0,"S":0},
                          "PPS":{"R":0,"P":0,"S":0},
                          "PSR":{"R":0,"P":0,"S":0},
                          "PSP":{"R":0,"P":0,"S":0},
                          "PSS":{"R":0,"P":0,"S":0},

                          "SRR":{"R":0,"P":0,"S":0},
                          "SRP":{"R":0,"P":0,"S":0},
                          "SRS":{"R":0,"P":0,"S":0},
                          "SPR":{"R":0,"P":0,"S":0},
                          "SPP":{"R":0,"P":0,"S":0},
                          "SPS":{"R":0,"P":0,"S":0},
                          "SSR":{"R":0,"P":0,"S":0},
                          "SSP":{"R":0,"P":0,"S":0},
                          "SSS":{"R":0,"P":0,"S":0},
                          
                       
      
    }
  if moves[0]!="":
    transition_matrix[0][moves[0]][prev_play]+=1

  if total_moves[0]>=3:
    moves[0]=guess[0]+prev_play+opponent_history[-2]
    val=max(transition_matrix[0][moves[0]],key = lambda k: transition_matrix[0][moves[0]][k])
    guess[0]=response[val]

  else:
    moves[0]=np.random.choice(["R","P","S"])+prev_play+np.random.choice(["R","P","S"])
    guess[0]=np.random.choice(["R","P","S"])

  total_moves[0]+=1
  
  return guess[0]
