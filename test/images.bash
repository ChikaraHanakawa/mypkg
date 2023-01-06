#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。
DIRECTORY=/src/mypkg/mypkg/face_images  #画像ファイルの絶対パス

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
if [ -d $DIRECTORY ]; then  #画像ファイルの存在確認
  echo "exit frame"
fi
