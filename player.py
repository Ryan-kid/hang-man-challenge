class player:
  def __init__(self, name, age, wins, losses):
    self.name = name
    self.age = age
    self.wins = wins
    self.losses = losses


  def __str__(self): 
     return ( f"Name: {self.name}, Age: {self.age}, Wins: {self.wins}, Losses: {self.losses}")






def login():
  User_name = input("Enter your name: ")
  User_age = input("Enter your age: ")

  player_model = player(User_name, User_age, 0, 0)

  return(player_model)