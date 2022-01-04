cat ~/ngrok/ngrok.log | grep -a url | tail -n 1 | sed -n "s/.*[u][r][l][=]\(\S*\).*$/\1/p"
