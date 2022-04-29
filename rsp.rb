$hands = { 1 => 'グー', 2 => 'チョキ', 3 => 'パー'}
$text = ""
show_hands = $hands.each { |num, hand | $text += "#{num}・・・#{hand}  "}

$computer_score = 0
$user_score = 0

def throw_hand
  puts "手を選んでください(#{$text.rstrip})>>>"
  #begin
  user_hand = gets.strip.to_i
  if [1, 2, 3].include?(user_hand)
    computer_hand = $hands.values.sample
    puts ""
    sleep 1
    puts "#{$user}は#{$hands[user_hand]}を出しました。"
    sleep 1
    puts "computerは#{computer_hand}を出しました。"
    [$hands[user_hand], computer_hand]
  else
    puts "1~3を半角で入力してください"
    throw_hand
  end
end

def who_win(user, computer) # 戻り値はあいこか勝者"
  if user == computer
    "あいこ"
  elsif user == 'グー' && computer == 'チョキ' || user == 'チョキ' && computer == 'パー' || user == 'パー' && computer == 'グー'
    $user
  else
    "computer" 
  end
end

def show_scores(winner, computer_score, user_score)
  if winner == "computer"
    computer_score += 1
  else
    user_score += 1
  end
  [computer_score, user_score]
end

def main
  puts '名前を入力してください>>>'
  $user = gets.strip
  puts ""
  puts "じゃんけんに1回勝つと1点獲得できます。先に3点とれば勝利です"
  sleep 2
  puts ""
  puts 'じゃんけんをはじめます'
  while $user_score < 3 && $computer_score < 3
    puts ""
    user_hand, computer_hand = throw_hand
    puts ""
    result = who_win(user_hand, computer_hand)
    while result == 'error'
      result = who_win(user_hand, computer_hand)
    end
      if result == "あいこ"
        puts "あいこです"
      else
        sleep 1
        puts "#{result}が勝ちました！"
        $computer_score, $user_score = show_scores(result, $computer_score, $user_score)
      end
    puts ""
    sleep 1
    puts "#{$user}のスコア: #{$user_score}, computerのスコア: #{$computer_score}"
    puts ""
    if $user_score == 3 || $computer_score == 3
      if $user_score == 3 then winner = $user 
      else winner = 'computer'
      end
        puts "勝者は#{winner}です！！"
    end
  end
end

main
