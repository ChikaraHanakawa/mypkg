# mypkg
こちらのリポジトリは、千葉工業大学先進工学部未来ロボティクス学科2年4Semesterの講義で取り扱われているものです.  
本リポジトリには、講義内で使用したパッケージがあり、`talker`と`listener`の２つのノードが含まれています.また、まだ実装段階に移っておりませんがOpenCVを利用したプログラムを作成中です.  
![test](https://github.com/ChikaraHanakawa/mypkg/actions/workflows/test.yml/badge.svg)  
↑ テスト結果を反映したバッジの画像が埋め込まれる。標準入力から読み込んだ数字を足す.  
# 本リポジトリの概要
`talker`というノードでパブリッシュし、`listener`というノードでサブスクライバしている.  
## 本リポジトリの使用方法
- terminal上にて以下のコマンドを実行  
```
$ git clone https://github.com/ChikaraHanakawa/mypkg.git
```
### talker.py
- countupというトピックを通じて、メッセージを送信する.メッセージの型は16ビットの符号付き整数.  
### listener.py
- countupというトピックからメッセージを受信する.また、`talker.py`が送信した順にterminalに出力する.  
### talk_listen.launch.py

# 実行方法(run)
1. 本リポジトリをclone後にterminal上に以下のコマンドを実行  
```
$ros2 run mypkg talker
```
2. 実行後に`Ctrl + Shift + t`を入力  
3. 新しいterminal(terminal2とする)に以下のコマンドを実行
```
$ros2 run mypkg listener
```
4. 以上を実行後、terminal2に出力  
5. `Ctrl + \`で終了  
## 実行結果
- terminal2に以下のように出力されれば成功  
```
[INFO] [1672469276.221867694] [listener]: Listen: 10
[INFO] [1672469276.717008380] [listener]: Listen: 11
[INFO] [1672469277.216945737] [listener]: Listen: 12
[INFO] [1672469277.716793518] [listener]: Listen: 13
[INFO] [1672469278.216785270] [listener]: Listen: 14
[INFO] [1672469278.716751346] [listener]: Listen: 15
[INFO] [1672469279.216718907] [listener]: Listen: 16
[INFO] [1672469279.716677141] [listener]: Listen: 17
[INFO] [1672469280.216946508] [listener]: Listen: 18
[INFO] [1672469280.716849977] [listener]: Listen: 19
[INFO] [1672469281.216855857] [listener]: Listen: 20
[INFO] [1672469281.716991408] [listener]: Listen: 21
[INFO] [1672469282.216778045] [listener]: Listen: 22
```
# 実行方法(launch)
1. terminalに以下のコマンドを実行  
```
$ros2 launch mypkg talk_listen.launch.py
```
2. `Ctrl + \`で終了  
## 実行結果
- 以下のように出力されれば成功
```
[listener-2] [INFO] [1672469459.934299271] [listener]: Listen: 0
[listener-2] [INFO] [1672469460.416664406] [listener]: Listen: 1
[listener-2] [INFO] [1672469460.916660351] [listener]: Listen: 2
[listener-2] [INFO] [1672469461.416669856] [listener]: Listen: 3
[listener-2] [INFO] [1672469461.916764066] [listener]: Listen: 4
[listener-2] [INFO] [1672469462.416812639] [listener]: Listen: 5
[listener-2] [INFO] [1672469462.916683554] [listener]: Listen: 6
[listener-2] [INFO] [1672469463.416726592] [listener]: Listen: 7
[listener-2] [INFO] [1672469463.916724492] [listener]: Listen: 8
[listener-2] [INFO] [1672469464.416683672] [listener]: Listen: 9
[listener-2] [INFO] [1672469464.916725295] [listener]: Listen: 10
```
# 必要なソフトウェア
- ROS
  - ROS2 foxy
- OS
  - Ubuntu 20.04 
# LICENSE
  - このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
  - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです
    - [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
  - © 2022 Chikara Hanakawa
