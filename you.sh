#!/usr/bin/env bash


read -p 'UesrName: ' username
read -p 'PassWord: ' passward
if [ ${username} == 'you' ];then
 if [ ${password} == '123' ];
  echo 'Load successfully' 
 else
  echo 'your password is false"
else
 echo"sb"
 fi
fi
