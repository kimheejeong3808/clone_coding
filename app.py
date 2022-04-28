import random

computer = random.randint(0, 2)
option = ['가위', '바위', '보']
computer_value = option[computer]

while True:
  player_value = input('가위 바위 보???')
  if player_value in option:
     print(player_value)
     print('를 선택했습니다')
     break

  print('값을 정확히 입력해주세요!')

print(f'플레이어는 {player_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다')

if computer_value == player_value:
    print('비겼습니다')
elif player_value == '가위':
    if computer_value == '바위':
        print('졌습니다')
    else:
        print('이겼습니다')
elif player_value == '바위':
    if computer_value =='보':
        print('졌습니다')
    else:
        print('이겼습니다')
elif player_value == '보':
    if computer_value == '가위':
       print('졌습니다')
    else:
        print('이겼습니다')



