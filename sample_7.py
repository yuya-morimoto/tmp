import tkinter as tk
import tkinter.messagebox as tmsg

from kadai2_func1 import generate_random_digits
from kadai2_func2 import includes_only_digits
from kadai2_func3 import convert_digitstring_to_list
from kadai2_func4 import count_hits
from kadai2_func5 import count_blows

# 1. グローバルな定数

NUMBER_OF_DIGITS = 5    # 数当てゲームで使う桁数


# 2. ボタンがクリックされたときの処理

def ButtonClick():
    # 2-1. 関数内で参照するグローバル定数とグローバル変数
    global NUMBER_OF_DIGITS
    global editbox
    global rirekibox

    # 2-2. テキスト入力欄に入力された文字列を取得する
    s_child = editbox.get()

    # 2-3. 入力された文字列の長さを判定する
    if len(s_child) != NUMBER_OF_DIGITS:
        tmsg.showerror("エラー", str(NUMBER_OF_DIGITS) + "桁の数字を入力してください")
        return

    # 2-4. 入力された文字列がすべて半角数字だけからなるかどうかを判定する
    if not includes_only_digits(s_child):
        tmsg.showerror("エラー", "数字ではありません")
        return

    # 2-5. 入力された半角数字だけからなる文字列を整数のリストに変換する
    l_child = convert_digitstring_to_list(s_child)

    # 2-6. ヒットを判定し、すべてヒットなら当たりでプログラムを終了する
    n_hits = count_hits(l_parent, l_child)
    if n_hits == NUMBER_OF_DIGITS:
        tmsg.showinfo("当たり", "おめでとうございます。当たりです")
        root.destroy()
        return

    # 2-7. 当たりでないなら、ブローを判定し、ヒット数とブロー数を表示する
    n_blows = count_blows(l_parent, l_child)
    rirekibox.insert(tk.END, s_child + "　／H:" + str(n_hits) + " B:" + str(n_blows) + "\n")


# 3. ゲームのメイン処理

# 3-1. 最初にランダムな数字を作成し、親が考えた数とする
l_parent = generate_random_digits(NUMBER_OF_DIGITS)
## デバッグ用表示（本番ゲームではコメントアウトすること）
print("デバッグ用表示: 親が考えた数=", l_parent)

# 3-2. 数当てゲームで使う桁数に合わせたウィンドウの横幅を計算する
rirekibox_width = 120 + 12 * NUMBER_OF_DIGITS
root_width = max(240, 20 + 24 * min(10, NUMBER_OF_DIGITS)) + rirekibox_width

# 3-2. ウィンドウを作る
root = tk.Tk()
root.geometry(str(root_width) + "x400")
root.title("数当てゲーム(" + str(NUMBER_OF_DIGITS) + "桁版)")

# 3-3. 履歴表示のテキストボックスを作る
rirekibox = tk.Text(root, font=("Helvetica", 14))
rirekibox.place(x = root_width - rirekibox_width, y = 0, width = rirekibox_width, height = 400)

# 3-4. ラベルを作る
label = tk.Label(root, text=str(NUMBER_OF_DIGITS) + "桁の数を入力してね", font=("Helvetica", 14))
label.place(x = 20, y = 20)

# 3-5. テキストボックスを作る
editbox = tk.Entry(width = min(10, NUMBER_OF_DIGITS), font=("Courier", 28))
editbox.place(x = 20, y = 60)

# 3-6. ボタンを作る
button = tk.Button(root, text = "チェック", font=("Courier", 14), command=ButtonClick)
button.place(x = 20, y = 120)

# 3-7. ウィンドウを表示する
root.mainloop()