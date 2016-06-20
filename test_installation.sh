#!/bin/sh
{
rm /opt/Watch-my-Pi/src/*

rmdir /opt/Watch-my-Pi/src

rmdir /opt/Watch-my-Pi

mkdir /opt/Watch-my-Pi/

cp -r src/ /opt/Watch-my-Pi

} || {
echo "fail"
mkdir /opt/Watch-my-Pi/

cp -r src/ /opt/Watch-my-Pi
}




