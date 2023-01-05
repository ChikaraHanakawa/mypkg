# mypkg
![test](https://github.com/ChikaraHanakawa/mypkg/actions/workflows/test.yml/badge.svg)  
![images](https://github.com/ChikaraHanakawa/mypkg/actions/workflows/images.yml/badge.svg)  
こちらのリポジトリは、千葉工業大学先進工学部未来ロボティクス学科2年4Semesterの講義で取り扱われているROS2のパッケージです。  
本リポジトリには、講義内で使用したパッケージがあり、`talker`と`listener`の２つのノードが含まれています。  
また、OpenCVを利用したwebカメラを用いて顔を検出してモザイク処理をするノードが含まれています。
# 本リポジトリの概要
`talker`というノードでパブリッシュし、`listener`というノードでサブスクライバしている。  
`image_publisher`というノードでパブリッシュし、`image_subscriber`というノードでサブスクライバしています。  
## 本リポジトリの使用方法
```
$ git clone https://github.com/ChikaraHanakawa/mypkg.git
```
### talker.py
- countupというトピックを通じて、メッセージを送信する。メッセージの型は16ビットの符号付き整数  
### listener.py
- countupというトピックからメッセージを受信する.また、`talker.py`が送信した順にterminalに出力  
### talk_listen.launch.py
- 本リポジトリに含まれている２つのノードを一度に立ち上げる事が可能
### images_pub.py
- `video_frames`というトピックを通じて、メッセージを送信する。メッセージの型は画像のImage
### images_sub.py
- video_framesというトピックを通じて、メッセージを受信する。人の顔を検出して、自動でモザイクをかける。また、モザイクをかけた状態で出力し、1フレーム毎に画像をface_imagesディレクトリに保存する。
# 実行方法 (run)
## talker&listener
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
## image_publisher&image_subscriber
1. 本リポジトリをclone後にterminal上に以下のコマンドを実行
```
$ros2 run mypkg img_publisher
```
2. 実行後に`Ctrl + Shift + t`を入力
3. 新しいterminal(terminal2とする)に以下のコマンドを実行
```
$ros2 run mypkg img_subscriber
```
4. 以上を実行後に`current_frame`というウィンドウが出力される
5. 人の顔を検出して、モザイクを勝手にかける
6. `Ctrl + \`で終了
7. terminal2で実行したディレクトリ内にface_imagesディレクトリが出来ているの確認する
8. 撮影した画像を確認する
```
$eog 00000.png
```
# 実行結果
## talker&listener
- terminal2に以下のように出力されれば成功  
```
[INFO] [1672469276.221867694] [listener]: Listen: 0
[INFO] [1672469276.717008380] [listener]: Listen: 1
[INFO] [1672469277.216945737] [listener]: Listen: 2
[INFO] [1672469277.716793518] [listener]: Listen: 3
[INFO] [1672469278.216785270] [listener]: Listen: 4
[INFO] [1672469278.716751346] [listener]: Listen: 5
[INFO] [1672469279.216718907] [listener]: Listen: 6
[INFO] [1672469279.716677141] [listener]: Listen: 7
[INFO] [1672469280.216946508] [listener]: Listen: 8
[INFO] [1672469280.716849977] [listener]: Listen: 9
[INFO] [1672469281.216855857] [listener]: Listen: 10
```
## image_publisher&image_subscriber
- terminal2にコマンドを実行後に、webカメラからの映像が出力されれば、成功
<img src = "https://user-images.githubusercontent.com/85380968/210791539-7e641175-8e1b-45c5-8700-2bbd5ebc8734.png" width="500">  

# 実行方法 (launch)
## talker&listener
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
# image_publisherとimage_subscriberの活用法
1. 一枚一枚をコマ送りのgif画像を作成する。  
出力しているウィンドウは、動画なので作りたいgif画像を画面を見ながら確認して、  
作成できるのがこのコードの強みだと思います。  
<img src="https://user-images.githubusercontent.com/85380968/210795307-b55c314a-4d76-4732-895a-7a84a46234ae.gif" width="500">

2. モザイクをかける部分をコメントアウトして、他の処理を入れる。また、OpenCVで配られている重みを用いて他の物を検出させるのも良いかと思います。  
# 動作確認済み環境
- ROS
  - ROS2 foxy
  - ROS2 Humble
- OS
  - Ubuntu 20.04 LTS  
  - Ubuntu 22.04 LTS  
# LICENSE
  - このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
  - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
    - [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
  - © 2022 Chikara Hanakawa
