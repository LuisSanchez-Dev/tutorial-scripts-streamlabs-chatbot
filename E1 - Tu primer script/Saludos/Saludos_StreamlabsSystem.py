ScriptName = "Saludos"
Description = "Saludar a todos"
Creator = "luissanchezdev"
Website = "twitch.tv/luissanchezdev"
Version = "1.0.0"

greeted_users = []

def Init():
  pass

def Execute(data):
  if data.IsChatMessage():
    if "hola" in data.Message.lower():
      user = data.UserName
      if user not in greeted_users:
        msg = "Hola " + user
        Parent.SendStreamMessage(msg)
        greeted_users.append(user)

def Tick():
  pass