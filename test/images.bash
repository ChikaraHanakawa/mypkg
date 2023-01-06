#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。
DIRECTORY=/face_images  #画像ファイルの絶対パス

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
#if [ -d $DIRECTORY ]; then  画像ファイルの存在確認
  #echo "exit frame"
#fi
if [ -n "$(ls -A $DIRECTORY)" ]; then
    echo "出力先にファイルが存在します。削除してください。=> $DSTDIR"
    exit 1
fi
