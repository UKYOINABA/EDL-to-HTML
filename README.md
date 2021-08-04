# EDLtoHTML
EDLとmp4の動画データからカットシートを自動で生成するプログラムです。  
実行後、  `EDLのフルパス`、`動画のフルパス`、`フレームレート`を指定し、`プロジェクト名`を入力すると、  
自動的にHTMLファイルが生成されます。  
Python3の実行環境が必要です。必要に応じて適宜インストールしてください。　 
**また、EDLはビデオレイヤ1レイヤ分のみ対応です。複数レイヤが重なっている場合は対応していません。(検討中)**

## 開発・動作確認環境:fearful:	
* MacOS 11.5(BigSur)

* Python3.8.3

* EDLはPremiere Pro CC 2021から出力されたEDLでしか動作確認してません:fearful:

## 実行環境構築

**Python3**のインストールがなされていない場合、以下のコマンドを実行してください

* HomeBrewのInstall
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
* Python3のインストール
```
brew install python
```
* 動作確認
以下を実行し `Python 3.X.X`のようになっていればインストール完了です。
```
python3 -V
```
## 追加のライブラリをpipでインストールする  
以下のコードを実行していってください。  

* HTMLを出力するための`Flask`のインストール
```
pip install flask
```
* 表データ操作用の`pandas`のインストール
```
pip install pandas
```
* 動画データ操作用の`cv2`のインストール
```
pip install cv2
```
# Usage:thumbsup:
ダウンロードしたEDLtoHTML.zipを解凍。
`terminal.app`を開き、解凍した`EDLtoHTML.pyのパス`を入力
```
python /user/hogehoge/hogehoge/EDLtoHTML.py
```
terminalから以下のように入力を求められるので適宜入力
```
EDL file path--->
```

```
Movie file path--->
```

```
frameRate?--->
```

```
Enter Project Name--->
```

処理が完了すると、動画ファイルと同じフォルダ内に`index.html`,`imagesフォルダ`が作成され、その内部に静止画データが生成される。  
`index.html`はカットシート形式になっており、そのまま印刷やPDFとして保存できる。



