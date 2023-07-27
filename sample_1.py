# 課題1. りんごとみかんを買ったときにお釣りを計算するプログラムをデバッグして完成させる
money  = 5000
apple  = 300
orange = 200
while True:
    flag = True
    # りんごとみかんを注文
    num_a = input("りんごを何個買いますか？> ")
    num_o = input("みかんを何個買いますか？> ")
    # 数字が入力されたかのチェック
    if not num_a.isdigit():
        print("数字ではありません")
        flag = False
    if not num_o.isdigit():
        print("数字ではありません")
        flag = False
    # 数字が入力されていれば購入金額を計算する
    if flag is True:
        total = apple * int(num_a) + orange * int(num_o)
        # 購入金額が所持金を超えていた場合
        if total > money:
            print("お金が足りません＞＜")
        else:
            money = money - total
            print("お釣りは" + str(money) + "円です")
            break