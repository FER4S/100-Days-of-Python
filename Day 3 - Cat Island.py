print('''
*******************************************************************************
                               __
                         _,-;'";`'-,.
                      _/',  `;  `;    `\\
      ,        _..,-''    '   `  `      `\\
     | ;._.,,-' .| |,_        ,,          `\\
     | `;'      ;' ;, `,   ; |    '  '  .   \\
     `; __`  ,'__  ` ,  ` ;  |      ;        \\
     ; (6_);  (6_) ; |   ,    \        '      |       /
    ;;   _,' ,.    ` `,   '    `-._           |   __//_________
     ,;.=..`_..=.,' -'          ,''        _,--''------''""
_pb__\,`"=,,,=="',___,,,-----'"----'_'_'_''-;''
-----------------------''"""\ \ '""""   )   /'
                              `\`,,,___/__/'_____,
                                `--,,,--,-,'""\\
                               __,,-' /'       `
                             /'_,,--''
                            | (
                             `'
*******************************************************************************
''')
print("Welcome to Cat Island.")
print("Your mission is to find the cat.") 

dir=input("You are at a cross road. Where do you want to go?  Type 'left' or 'right'\n").lower()
if dir=='left':
  action=input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boad or 'swim' to swim accros\n").lower()
  if action=='wait':
    door=input("You arrived to the island unharmed. There is a house with 3 door. One red, yellow and blue. Choose one!\n").lower()
    if door=='red':
      print("Burnt by fire. GAME OVER")
    elif door=='blue':
      print("You entered the room of beasts. GAME OVER")
    elif door=='yellow':
      print('''
      YOU FOUND THE CAT!!!!!
                               |        |
                               |\      /|
                               | \____/ |
                               |  /\/\  |
                              .'___  ___`.
                             /  \|/  \|/  \\
            _.--------------( ____ __ _____)
         .-' \  -. | | | | | \ ----\/---- /
       .'\  | | / \` | | | |  `.  -'`-  .'
      /`  ` ` '/ / \ | | | | \  `------'\\
     /-  `-------.' `-----.       -----. `---.
    (  / | | | |  )/ | | | )/ | | | | | ) | | )
     `._________.'_____,,,/\_______,,,,/_,,,,/ 
      ''')
    else:
      print('GAME OVER. YOU LOST!')
  else: 
    print('You get attacked by by an angry trout. GAME OVER')
else:
  print('You fell into a hole. GAME OVER')