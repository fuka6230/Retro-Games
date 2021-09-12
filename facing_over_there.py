import random


# じゃんけん
def rps():
    num_to_hand = {1: 'グー', 2: 'チョキ', 3: 'パー'} 
    global winner
    global loser

    print('じゃんけんを始めます')

    while True:
        try:
            my_hand_num = int(input('数字を入力してください(1: グー, 2: チョキ, 3: パー):'))
        except ValueError:
            print('入力が間違っています。半角の1~4を入力してください。')
            continue
        else:
            if not my_hand_num in num_to_hand.keys():
                print('入力が間違っています。半角の1~4を入力してください。')
                continue       
        
        com_hand_num = random.choice((1, 2, 3))

        print(f'あなたは{num_to_hand[my_hand_num]}を出しました')
        print(f'コンピュータは{num_to_hand[com_hand_num]}を出しました')
    
        # 判定
        if my_hand_num == com_hand_num: # あいこ
            print('あいこです')
        elif (my_hand_num == 1 and com_hand_num == 2)\
            or (my_hand_num == 2 and com_hand_num == 3)\
            or (my_hand_num == 3 and com_hand_num == 1): # プレイヤーが勝つ場合
            print('あなたの勝ちです')
            winner = 'player'
            loser = 'computer'
            break
        else: # コンピューターが勝つ場合
            print('コンピュータの勝ちです')
            winner = 'computer'
            loser = 'player'
            break


# あっち向いてホイ
def fot(winner, loser):
    num_to_dir = {1: '上', 2: '下', 3: '左', 4:'右'}
    global result  

    print('あっち向いてホイを始めます。')
    
    while True:
        try:
            
            my_dir = int(input('数字を入力してください(1: 上, 2: 下, 3:左, 4:右)'))
        except ValueError:
            print('入力が間違っています。半角の1~3を入力してください。')
            continue
        else:
            if not my_dir in num_to_dir.keys():
                print('入力が間違っています。半角の1~3を入力してください。')
                continue
            else:
                break
    com_dir = random.choice((1, 2, 3, 4))
    
    if winner == 'player':
        winner = 'あなた'
        winner_dir = num_to_dir[my_dir]
        loser = 'コンピュータ'
        loser_dir = num_to_dir[com_dir]
    else:
        winner = 'コンピュータ'
        winner_dir = num_to_dir[com_dir]
        loser = 'あなた'
        loser_dir = num_to_dir[my_dir]

    print(f'{winner}は{winner_dir}を指しました。')
    print(f'{loser}は{loser_dir}を向きました。')

    # 判定　
    if my_dir == com_dir:
        print(f'{winner}の勝ちです！')
        result = 'end'
    else:
        result = 'continue'


# 実行  
while True:
    rps()
    fot(winner, loser)
    if result == 'end':
        break
