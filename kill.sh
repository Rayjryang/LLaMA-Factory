ps aux | grep launcher.py | grep -v grep | awk '{print $2}' | xargs kill -9
ps aux | grep llamafactory-cli | grep -v grep | awk '{print $2}' | xargs kill -9
