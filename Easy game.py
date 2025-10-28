import random 
def get_choices():
  player_choice = input("Enter your choice:")
  computer_choice = ['paper','rock','scissor']
  rand_comp_choice = random.choice(computer_choice)
  choices = {'player' : player_choice , 'computer' : rand_comp_choice}

  return choices 
  
def check_win(player , computer):
  print(f' you chose {player} , computer chose {computer}')
  if player == computer:
    return 'tie'
  elif player == 'rock':
    if computer == 'paper':
      return 'computer wins'
    else: 
      return 'player wins'
  elif player == 'paper': 
    if computer == 'rock':
      return 'player wins'
    else:
      return 'computer wins'
  elif player == 'scissor':
    if computer == 'paper':
      return 'player wins'
    else:
       return 'computer wins'
    
  else:
    return 'Invalid input'

choices = get_choices()
result = check_win(choices['player'],choices['computer'])
print(result)

  
  
  
  


  
  