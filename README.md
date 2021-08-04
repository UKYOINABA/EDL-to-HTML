# EDLtoHTML
EDLとmp4の動画データからカットシートを自動で生成するプログラムです。実行後、EDLのフルパス、動画のフルパス、動画のフレームレートを指定し、プロジェクト名を入力すると、自動的にHTMLファイルが生成されます。

## 開発・動作確認環境:fearful:	
*- MacOS 11.5(BigSur)*

*- Python3.8.3*

## Usege
追加が必要なライブラリは以下の通りです
```
- flask
- pandas
- cv2
```
Python3がインストールがなされていない場合、以下のコマンドを実行してください

### HomeBrewのInstall
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
### Python3のインストール
```
brew install python
```
### 動作確認
以下を実行し `Python 3.X.X`のようになっていればインストール完了です。
```
python3 -V
```
### 追加のライブラリをpipでインストールする  
以下のコードを実行していってください。  

HTMLを出力するための`Flask`のインストール
```
pip install flask
```
表データ操作用の`pandas`のインストール
```
pip install pandas
```
動画データ操作用の`cv2`のインストール
```
pip install cv2

