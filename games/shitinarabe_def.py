import random
import time
import re

marks = ('スペード', 'ハート', 'ダイヤ', 'クローバー') # 全てのマーク
numbers = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K') #全ての数字
num_order = []
for mark in marks:
    for num in numbers:
        num_order.append(mark+num)

all_cards_to_numbers = {} # 全てのカードに通し番号を付ける
n = 1
for mark in ('スペード', 'ハート', 'ダイヤ', 'クローバー'):
    for m in numbers:
        value = mark + m
        all_cards_to_numbers[n] = value
        n += 1

def print_ba(spade, heart, dia, clover): # 場を表示
    print(f'スペード:    {spade}')
    print(f'ハート:      {heart}')
    print(f'ダイヤ:      {dia}')
    print(f'クローバー:  {clover}')


def card_and_number(user_cards): # カードを数字を対応付け
    card_choice = {}
    for user_card, number in zip(user_cards, range(1, 14)):
        card_choice[number] = user_card
    return card_choice

def choice_card(card_choice): # userがカードを選ぶ
    time.sleep(0.5)
    choiced_card = input(card_choice)
    if choiced_card == '0':
        return 'PASS'   
    else:
        return choiced_card

def number_to_card(number, user_cards): # 数字からカードに変換
    dic = card_and_number(user_cards)
    return dic[number]

def player_to_ba(user_cards, card, ba_spade, ba_heart, ba_dia, ba_clover): # カードをプレイヤーから場に移す

    if 'A' in card:
        for mark, ba_mark in zip(('スペード', 'ハート', 'ダイヤ', 'クローバー'), (ba_spade, ba_heart, ba_dia, ba_clover)):
            if mark in card:
                if ba_mark[1] == 0 and ba_mark[12] == 0:
                    return 'NG' # 場に出せない場合
        if 'スペード' in card:
            ba_spade[0] = 'A'
        elif 'ハート' in card:
            ba_heart[0] = 'A'
        elif 'ダイヤ' in card:
            ba_dia[0] = 'A'
        elif 'クローバー' in card:
            ba_clover[0] = 'A'  
    elif 'J' in card:
        for mark, ba_mark in zip(('スペード', 'ハート', 'ダイヤ', 'クローバー'), (ba_spade, ba_heart, ba_dia, ba_clover)):
            if mark in card:
                if ba_mark[9] == 0 and ba_mark[11] == 0:
                    return 'NG' # 場に出せない場合     
        if 'スペード' in card:
            ba_spade[10] = 'J'
        elif 'ハート' in card:
            ba_heart[10] = 'J'
        elif 'ダイヤ' in card:
            ba_dia[10] = 'J'
        elif 'クローバー' in card:
            ba_clover[10] = 'J'
    elif 'Q' in card:
        for mark, ba_mark in zip(('スペード', 'ハート', 'ダイヤ', 'クローバー'), (ba_spade, ba_heart, ba_dia, ba_clover)):
            if mark in card:
                if ba_mark[10] == 0 and ba_mark[12] == 0:
                    return 'NG' # 場に出せない場合 
        if 'スペード' in card:
            ba_spade[11] = 'Q'
        elif 'ハート' in card:
            ba_heart[11] = 'Q'
        elif 'ダイヤ' in card:
            ba_dia[11] = 'Q'
        elif 'クローバー' in card:
            ba_clover[11] = 'Q'
    elif 'K' in card:
        for mark, ba_mark in zip(('スペード', 'ハート', 'ダイヤ', 'クローバー'), (ba_spade, ba_heart, ba_dia, ba_clover)):
            if mark in card:
                if ba_mark[11] == 0 and ba_mark[0] == 0:
                    return 'NG' # 場に出せない場合                   
        if 'スペード' in card:
            ba_spade[12] = 'K'
        elif 'ハート' in card:
            ba_heart[12] = 'K'
        elif 'ダイヤ' in card:
            ba_dia[12] = 'K'
        elif 'クローバー' in card:
            ba_clover[12] = 'K'
    else:
        card_num = re.sub(r'\D', '', card) 
        for mark, ba_mark in zip(('スペード', 'ハート', 'ダイヤ', 'クローバー'), (ba_spade, ba_heart, ba_dia, ba_clover)):
            if mark in card:
                if ba_mark[int(card_num) - 2] == 0 and ba_mark[int(card_num)] == 0:
                    return 'NG' # 場に出せない場合
        if 'スペード' in card:
            ba_spade[int(card_num) - 1] = int(card_num)
        elif 'ハート' in card:
            ba_heart[int(card_num) - 1] = int(card_num)
        elif 'ダイヤ' in card:
            ba_dia[int(card_num) - 1] = int(card_num)
        elif 'クローバー' in card:
            ba_clover[int(card_num) - 1] = int(card_num)

    user_cards.remove(card) 
    return user_cards
    
def can_play_card(card, ba_spade, ba_heart, ba_dia, ba_clover):   
    for mark in ('スペード', 'ハート', 'ダイヤ', 'クローバー'):
        if mark in card:            
            if 'A' in card:
                return 'OK'
            r = re.sub(r'\D', '', card)
            



def user_play_card_main(user_cards, user_pass_counter, ba_spade, ba_heart, ba_dia, ba_clover): # userがカードを選んで場に出す
    print('あなたのターンです')
    print('どのカードを出しますか？（数字で選択）（パスは0を入力）') 
    user_cards = sorted(user_cards, key=num_order.index) 

    while True:   
        choiced_card = choice_card(card_and_number(user_cards))
        if choiced_card == 'PASS':
            user_pass_counter += 1
            return 'PASS'
        else:
            card = number_to_card(int(choiced_card), user_cards)
            NG_cheker = player_to_ba(user_cards, card, ba_spade, ba_heart, ba_dia, ba_clover)
            if NG_cheker == 'NG':
                print('そのカードは出せません')            
            else:
                return user_cards







def com_play_card_main(player, player_cards, pass_counter, ba_spade, ba_heart, ba_dia, ba_clover): # computerが場にカードを出す
    print(f'{player} のターンです')

    cards_in_ba_num = [] # 場に出ているカードの通し番号
    for ba_card, num in zip((ba_spade + ba_heart + ba_dia + ba_clover), range(1, 53)):
        if ba_card != 0:
            cards_in_ba_num.append(num)

    next_keys = [] # 場に出ているカードの隣の通し番号
    for card_key in cards_in_ba_num:       
        if card_key == 1 or card_key == 14 or card_key == 27 or card_key == 40: # カードが左端の場合
            next_keys.append(card_key + 1)
            next_keys.append(card_key + 12)
        elif card_key == 13 or card_key == 26 or card_key == 39 or card_key == 52: # カードが右端の場合
            next_keys.append(card_key - 1)
            next_keys.append(card_key - 12)
        else:
            next_keys.append(card_key - 1)
            next_keys.append(card_key + 1)
        
    
    
    player_cards_num = [k for k, v in all_cards_to_numbers.items() if v in player_cards] # playerの持っているカードの通し番号
    
    can_play_cards = list(set(next_keys) & set(player_cards_num)) # 出せるカード

    if can_play_cards == []:
        pass_counter += 1
        return 'PASS'
        
    else:
        # 出せるカードからランダムに選ぶ
       play_card = all_cards_to_numbers[random.choice(can_play_cards)]
       print(play_card)
       result = player_to_ba(player_cards, play_card, ba_spade, ba_heart, ba_dia, ba_clover)
       if result == []:
           return 'FINISH'





           
