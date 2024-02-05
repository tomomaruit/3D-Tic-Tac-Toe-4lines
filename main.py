# 乱数生成検証用の random モジュール
# import random
print("立体四目ゲーム!")

player_number = 1 # 二人のプレイヤーのうち．現在どちらのターンかを管理

# ゲームを行うにあたって、石の位置を管理する二次元配列を作成
layer1 = [[0 for j in range(4)] for k in range(4)] # 1段目
layer2 = [[0 for j in range(4)] for k in range(4)] # 2段目
layer3 = [[0 for j in range(4)] for k in range(4)] # 3段目
layer4 = [[0 for j in range(4)] for k in range(4)] # 4段目

# 現在置いている石の個数を数える変数
stone = 0

# ゲーム継続中に繰り返すための処理，全部石が埋まったら終了
while stone != 64:
    # 現在のターンの表示部分
    if player_number ==1:
        print("\n---プレイヤー1 記号:@ のターン---")
    elif player_number ==2:
        print("\n---プレイヤー2 記号:O のターン---")

    print("{}手目".format(stone+1))
    # 乱数生成を用いたテストを有効にする場合，冒頭の import random を有効化し，
    # ゲーム用入力部分を無効化して乱数生成を用いたテスト部分を有効化することで動作する．
    
    # ゲーム用入力部分ここから
    put_position = input("石を置く位置を入力してください(例:1,2)．終了する場合は(0,0)を入力してください．>") # 石の位置の入力を求める
    
    # カンマが含まれているかの検証
    if "," in put_position:
        x,y = map(int, put_position.split(',')) # 入力された石の位置を,を検出してx,yに代入する
    else: # カンマが含まれていない（入力形式が異なる）とき
        print("カンマが検出できませんでした．ゲームを終了します．")
        exit()
    # ゲーム用入力部分ここまで

    """
    # 乱数生成を用いたテスト部分ここから
    x = random.randint(1, 4)
    y = random.randint(1, 4)
    # 乱数生成を用いたテスト部分ここまで
    """
    
    # 終了を意味する位置が入力されたとき
    if x == 0 and y == 0:
        print("終了が検出されました，ゲームを終了します．")
        exit() # 強制終了

    # 範囲外入力が検出されたとき
    if x < 1 or 4< x or y < 1 or 4 < y:
        print("入力された位置に石は置けません．ゲームを終了します．")
        exit() # 強制終了

    # 石を置く，つまり配列の要素をを書き換える部分
    j = 1 # 1段目から検証
    while j <=  4: # 特定の条件を満たしたときにのみ段数を増加させたいので，for文ではなくwhile文を用いた
        judgelayer = globals()['layer' + str(j)] # 現在の段数の配列を定義
        if judgelayer[x-1][y-1] == 0: # 石を置こうとしている位置の要素が0（=石が置かれていない）なら
            judgelayer[x-1][y-1] = player_number # プレイヤーの番号の石を置く(1 or 2)
            print("石を({}段目, {}行目, {}列目)に置きました．\n".format(j, x, y)) # 石を置いた位置を表示
            stone = stone + 1 # 置いた石の個数を増加
            
            # プレイヤーチェンジ
            if player_number ==1:
                player_number = 2
            elif player_number ==2:
                player_number = 1
            break # ループ脱出，出力フェーズへ
        
        elif judgelayer[x-1][y-1] == 1 or 2: # 置こうとしている位置に既に石が置かれていたら
            j = j + 1 # 段数を増加させる
        if judgelayer[x-1][y-1] != 0 and j > 4: # 段数を増加させて、最上段（4段目）まで全て埋まっているなら
            print("この位置はすべて石が埋まっています．別の位置を選択してください") # 別の位置での入力を要求
            break # ループ脱出

    # 現在の石の状況出力部分
    print("---現在の状況---")
    print("---凡例---") # 凡例の表示
    print("-プレイヤー1：@\n-プレイヤー2：O\n-石が置かれていない場所：_")
    print("-現在{}手目\n".format(stone)) # 現在までの手数を表示
    for l in range(1,5): # 1から4の範囲でlを1ずつ増加させながら繰り返す
        print("【{}段目】".format(l)) # 表示している段数
        print("  1234 列") # 列数の表示
        outputlayer = globals()['layer' + str(l)] # 出力する段の配列を定義
        for m in range (4): # 行の分繰り返す
            print("{} ".format(m+1),end = '') # 行数の表示
            for n in range(4):
                if (outputlayer[m][n] == 0): # 0なら半角の#を出力
                    print('_',end = '')
                elif (outputlayer[m][n] == 1): # 1なら半角の@を出力
                    print('@',end = '')
                elif (outputlayer[m][n] == 2): # 2なら半角，大文字のO（オー）を出力
                    print('O',end = '')
            print("\n",end = '') # 1行分の出力完了したので改行する
        print("行\n",end = '') # 全ての行の出力が完了したので単位を表示
    print("\n",end = '') # 状況の出力完了したので改行する

    # 検証部分
    # 同一段内，行方向に4個ならんでいるかを検証
    # README.md における対応 1.1
    for l in range(1,5):
        nowlayer = globals()['layer' + str(l)] # 検索対象の配列を定義
        for m in range(4):
            player1 = 0 # 条件を満たす石のカウンターを定義
            player2 = 0
            for n in range(4):
                if (nowlayer[m][n] == 1): 
                    player1 = player1 + 1
                if (nowlayer[m][n] == 2):
                    player2 = player2 + 1
            if (player1 == 4): # 条件を満たす石の個数が4個の場合
                print("{}段目の{}行目が揃いました！{}手でプレイヤー1の勝ち！\nゲームを終了します".format(l,m+1,stone))
                exit()
            if (player2 == 4):
                print("{}段目の{}行目が揃いました！{}手でプレイヤー2の勝ち！\nゲームを終了します".format(l,m+1,stone))
                exit()

    # 同一段内，列方向に4個ならんでいるか検証
    # README.md における対応 1.2
    for l in range(1,5):
        nowlayer = globals()['layer' + str(l)] # 検索対象の配列を定義
        for m in range(4):
            player1 = 0 # 条件を満たす石のカウンターを定義
            player2 = 0
            for n in range(4):
                if (nowlayer[n][m] == 1):
                    player1 = player1 + 1
                if (nowlayer[n][m] == 2):
                    player2 = player2 + 1
            if (player1 == 4): # 条件を満たす石の個数が4個の場合
                print("{}段目の{}列目が揃いました！{}手でプレイヤー1の勝ち！\nゲームを終了します".format(l,m+1,stone))
                exit()
            if (player2 == 4):
                print("{}段目の{}列目が揃いました！{}手でプレイヤー2の勝ち！\nゲームを終了します".format(l,m+1,stone))
                exit()

    # 同一平面内，斜め方向に4個ならんでいるか検証
    # README.md における対応 1.3.1
    for l in range (1,5):
        nowlayer = globals()['layer' + str(l)]
        player1 = 0
        player2 = 0
        for m in range(4):
            if (nowlayer[m][m] == 1):
                player1 = player1 + 1
            if (nowlayer[m][m] == 2):
                player2 = player2 + 1
        if (player1 == 4):
            print("{}段目で斜め（\）に揃いました！{}手でプレイヤー1の勝ち！\nゲームを終了します".format(l,stone))
            exit()
        if (player2 == 4):
            print("{}段目で斜め（\）に揃いました！{}手でプレイヤー2の勝ち！\nゲームを終了します".format(l,stone))
            exit()
    
    # 同一平面内，斜め方向に4個ならんでいるか検証
    # README.md における対応 1.3.2
    for l in range (1,5):
        nowlayer = globals()['layer' + str(l)]
        player1 = 0
        player2 = 0
        for m in range(4):
            if (nowlayer[m][3-m] == 1):
                player1 = player1 + 1
            if (nowlayer[m][3-m] == 2):
                player2 = player2 + 1
        if (player1 == 4):
            print("{}段目で斜め（/）に揃いました！{}手でプレイヤー1の勝ち！\nゲームを終了します".format(l,stone))
            exit()
        if (player2 == 4):
            print("{}段目で斜め（/）に揃いました！{}手でプレイヤー2の勝ち！\nゲームを終了します".format(l,stone))
            exit()

    layer4_judge = 0 # 4段目の要素が全て0かどうか検証する際に使用するフラグ
    for m in range(4): # 行方向検証
        for n in range (4): # 列方向検証
            if (layer4[m][n] != 0): # 0以外なら
                layer4_judge = 1 # フラグ更新
                break # ループ脱出
            
    if (layer4_judge == 1):
        # 同一位置，段違いで4個ならんでいるか検証
        # README.md における対応 2
        for m in range(4):
            for n in range(4):
                player1 = 0
                player2 = 0
                if (layer4[m][n] == 1):
                    player1 = player1 + 1
                    for l in range (3,0,-1):
                        nowlayer = globals()['layer' + str(l)]
                        if (nowlayer[m][n] == 1):
                            player1 = player1 + 1
                    if (player1 == 4):
                        print("{}行目{}列目で段違いで揃いました！{}手でプレイヤー1の勝ち！\nゲームを終了します".format(m+1,n+1,stone))
                        exit()
                if (layer4[m][n] == 2):
                    player2 = player2 + 1
                    for l in range (3,0,-1):
                        nowlayer = globals()['layer' + str(l)]
                        if (nowlayer[m][n] == 2):
                            player2 = player2 + 1
                    if (player2 == 4):
                        print("{}行目{}列目で段違いで揃いました！{}手でプレイヤー2の勝ち！\nゲームを終了します".format(m+1,n+1,stone))
                        exit()

        # 異なる位置，複数の段を経由する場合の判定
        # README.md における対応 3.1
        # 4段目4行目と1段目1行目間の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
        for judge_player in range (1,3):
            for m in range(4):
                if (layer1[0][m] ==  judge_player and layer2[1][m] == judge_player and layer3[2][m] == judge_player and layer4[3][m] == judge_player):
                    print("4段目4行目{}列目と1段目1行目{}列目の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(m+1,m+1,stone,judge_player))
                    exit()
        
        # README.md における対応 3.2
        # 4段目1行目と1段目4行目間の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
        for judge_player in range (1,3):
            for m in range(4):
                if (layer1[3][m] ==  judge_player and layer2[2][m] == judge_player and layer3[1][m] == judge_player and layer4[0][m] == judge_player):
                    print("4段目1行目{}列目と1段目4行目{}列目の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(m+1,m+1,stone,judge_player))
                    exit()
        
        # README.md における対応 3.3
        # 4段目4列目と1段目1列目間の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
            for m in range(4):
                if (layer1[m][0] ==  judge_player and layer2[m][1] == judge_player and layer3[m][2] == judge_player and layer4[m][3] == judge_player):
                    print("4段目{}行目4列目と1段目{}行目1列目の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(m+1,m+1,stone,judge_player))
                    exit()
        
        # README.md における対応 3.4
        # 4段目1列目と1段目4列目間の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
        for judge_player in range (1,3):
            for m in range(4):
                if (layer1[m][3] ==  judge_player and layer2[m][2] == judge_player and layer3[m][1] == judge_player and layer4[m][0] == judge_player):
                    print("4段目{}行目1列目と1段目{}行目4列目の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(m+1,m+1,stone,judge_player))
                    exit()

        for judge_player in range (1,3):
            # README.md における対応 3.5
            # 4段目4行目4列と1段目1行目1列の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
            if (layer1[0][0] == judge_player and layer4[3][3] == judge_player):
                if (layer2[1][1] == judge_player and layer3[2][2] == judge_player):
                    print("4段目4行目4列と1段目1行目1列の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(stone,judge_player))
                    exit()
            # README.md における対応 3.6
            # 4段目1行目1列と1段目4行目4列間の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
            elif (layer1[3][3] == judge_player and layer4[0][0] == judge_player):
                if (layer2[2][2] == judge_player and layer3[1][1] == judge_player):
                    print("4段目1行目1列と1段目4行目4列の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(stone,judge_player))
                    exit()
            # README.md における対応 3.7
            # 4段目4行目1列と1段目1行目4列間の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
            elif (layer1[0][3] == judge_player and layer4[3][0] == judge_player):
                if (layer2[1][2] == judge_player and layer3[2][1] == judge_player):
                    print("4段目4行目1列と1段目1行目4列の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(stone,judge_player))
                    exit()
            # README.md における対応 3.8
            # 4段目1行目4列と1段目4行目1列間の検証：石が置かれているとき，異なる位置，複数の段を経由して4個ならんでいないか検証
            elif (layer1[3][0] == judge_player and layer4[0][3] == judge_player):
                if (layer2[2][1] == judge_player and layer3[1][2] == judge_player):
                    print("4段目1行目4列と1段目4行目1列の間が揃いました！{}手でプレイヤー{}の勝ち！\nゲームを終了します".format(stone,judge_player))
                    exit()

# 全ての石が置かれ，かつ決着がつかなかった場合の動作
if (stone == 64):
    print("全ての石が置かれました，決着がつきませんでした．\nゲームを終了します")
    exit()