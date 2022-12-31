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

## 実行方法(ros2 run)
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
## 実行結果
- 
5. `Ctrl + \`で終了  
## 実行方法(ros2 launch)
1. terminalに以下のコマンドを実行  
```
$ros2 launch mypkg talk_listen.launch.py
```
2. `Ctrl + \`で終了  
## 実行結果
- 
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
