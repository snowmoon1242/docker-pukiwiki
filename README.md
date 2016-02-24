# FeedConv.cgi の書き換え
以下の行を取得したいATOMフィードのURLに書き換える

```
$feedurl = "YOUR_OWN_FEED_URL";
```

例えば、取得したいURLが、Redmineのチケット状況のATOMフィード
「http://192.168.11.100:8080/projects/hoge/issues.atom?c[]=tracker」
だとすると、
```
$feedurl = "http://192.168.11.100:8080/projects/hoge/issues.atom?c[]=tracker";
```

# Docker Build
sudo docker build -t snowmoon6467/pukiwiki:1.5.0 pukiwiki150/

# コンテナ起動
sudo docker run --name pukiwiki150 -p 10080:80 -d snowmoon6467/pukiwiki:1.5.0

# Pukiwiki動作確認
ブラウザで接続して動作を確認する。
動作しているホストが「192.168.11.100」の場合、

http://192.168.11.100:10080/

# CGI動作確認
http://192.168.11.210:10081/cgi-bin/FeedConv.cgi

# PukiwikiのShowRSSでATOMフィード表示
```
|SIZE(14):BGCOLOR(WhiteSmoke):タイトル|SIZE(14):BGCOLOR(White):#showrss(http://192.168.11.210:10080/cgi-bin/FeedConv.cgi,default,5,1)|
```
