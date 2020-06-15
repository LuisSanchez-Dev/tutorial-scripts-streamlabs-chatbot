ScriptName = "Peleas"
Description = "Pelear con los demas"
Creator = "luissanchezdev"
Website = "twitch.tv/luissanchezdev"
Version = "1.0.0"

def Init():
  pass

def Execute(data):
  if data.IsChatMessage():
    command = data.GetParam(0)
    if command == "!pelear":
      if data.GetParamCount() != 2:
        usage = "Uso: !pelear <nombre>"
        Parent.SendStreamMessage(usage)
        return
      user = data.UserName
      enemy = data.GetParam(1)

      if Parent.GetRandom(0, 2):
        winner = user
        loser = enemy
      else:
        winner = enemy
        loser = user

      msg = winner + " destrozo a " + loser + "!!!"
      Parent.SendStreamMessage(msg)
    elif command == "!abrazar":
      # codigo
      pass
    
def Tick():
  pass