import random
import time
import shitinarabe_def as shiti_def

players_cards = []
cards_list = [] # 全てのカード
marks = ('スペード', 'ハート', 'ダイヤ', 'クローバー') # 全てのマーク
numbers = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K') #全ての数字
ba_spade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ba_heart = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ba_dia = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ba_clover = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
order = {}
user_pass_counter = 0 # パスした回数
player1_pass_counter = 0
player2_pass_counter = 0
player3_pass_counter = 0
num_order = []
for mark in marks:
    for num in numbers:
        num_order.append(mark+num)

# all_cardsの中身の作成
for mark in marks:
    for number in numbers:
        card = mark + number
        cards_list.append(card)


players = ('player1', 'player2', 'player3', 'あなた')

print('カードを配ります')
time.sleep(1)

players_list = list(players)
for n in range(1, 5): # カードを配る
    player = random.choice(players_list)
    player_cards = random.sample(cards_list, 13)

 

    if player == 'player1':
        player1_cards = player_cards
    elif player == 'player2':
        player2_cards = player_cards
    elif player == 'player3':
        player3_cards = player_cards
    else:
        user_cards = player_cards
        print(f'あなたのカード: {sorted(user_cards, key=num_order.index)}')
        time.sleep(1)

    players_list.remove(player)
    cards_list = set(cards_list) ^ set(player_cards)
    if 'joker' in cards_list:
        player_cards = cards_list.remove('joker')

n = 1
m = 0
for cards, player in zip([player1_cards, player2_cards, player3_cards, user_cards] * 2, players * 2):
    if m == 0 and ('ダイヤ7' in cards):
        order[n] = player
        n += 1
        m = 1
    elif m == 1:
        order[n] = player
        n += 1
        if n == 5:
            break
    else:
        continue
    

        


print('7のカードを場に出します')
time.sleep(1)

for player_cards in (player1_cards, player2_cards, player3_cards, user_cards): # 7のカードを場に出す
    if 'スペード7' in player_cards:
        ba_spade[6] = 7
        player_cards.remove('スペード7')
    if 'ハート7' in player_cards:
        ba_heart[6] = 7
        player_cards.remove('ハート7')
    if 'ダイヤ7' in player_cards:
        ba_dia[6] = 7
        player_cards.remove('ダイヤ7')
    if 'クローバー7' in player_cards:
        ba_clover[6] = 7
        player_cards.remove('クローバー7')

def ba_and_usercards(user_cards): # 場とuserのカードを表示
    shiti_def.print_ba(ba_spade, ba_heart, ba_dia, ba_clover)
    print(f'あなたのカード: {sorted(user_cards, key=num_order.index)}')

ba_and_usercards(user_cards)
time.sleep(1)
print(f'順番:   {order}')

n = 1
for _ in range(1, 200):
    time.sleep(1)
    player = order[n]
    if player == 'あなた':          
        result = shiti_def.user_play_card_main(user_cards, user_pass_counter, ba_spade, ba_heart, ba_dia, ba_clover)
        if result != 'PASS':
            user_cards = result
            if user_cards == []:
                print('あなたの勝ちです！')
                break
    else:
        if player == 'player1':
            player_pass_counter = player1_pass_counter
            player_cards = player1_cards
        elif player == 'player2':
            player_pass_counter = player2_pass_counter
            player_cards = player2_cards
        else:
            player_pass_counter = player3_pass_counter
            player_cards = player3_cards

        result = shiti_def.com_play_card_main(player, player_cards, player_pass_counter, ba_spade, ba_heart, ba_dia, ba_clover)
        shiti_def.print_ba(ba_spade, ba_heart, ba_dia, ba_clover)
        if result == 'FINISH' :
            print(player + 'の勝ちです！')
            break
    if n == 4:
        n = 1
    else:
        n += 1




