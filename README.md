# Pyxel_trick_or_track
<img width="953" alt="image_home" src="https://user-images.githubusercontent.com/101140119/200431082-d521a164-988b-44f0-9b53-20f6ec9cadd0.png">

# はじめに
(Qiitaへ投稿した記事をそのまま転載しています．以下が記事へのリンクです．)
15000views トレンド1位ありがとうございます！！
- [【Python / Pyxel】Webで遊べてSNSに共有できる，レトロゲームを作ってみた．](https://qiita.com/rwatanab1999/items/d5c0bb876f0b44cac2f0)

はじめまして，
[42tokyo Advent Calendar 2022](https://qiita.com/advent-calendar/2022/42tokyo)の8日目を担当する、changです．
今回は，Python向けのレトロゲームエンジンであるPyxelを使って，簡単なミニゲームを制作しました．Pyxelはゼロベースで学習しながらの制作でした．その際に学んだこと，役に立った知識や文献等を，時系列を追って簡単にまとめます．尚，今回はサウンドや効果音周りにまでは手を広げず，あくまでも最低限の基本要素のみとさせていただきます．
Pyxelをゼロから始めてみたい方の参考になれば幸いです．

# 目次
<!-- タイトルとアンカー名を編集 -->
1. [Pyxelとは](#pyxelとは)
2. [制作したゲーム](#制作したゲーム)
3. [環境構築とマニュアル](#環境構築とマニュアル)
4. [プログラムの基本構造](#プログラムの基本構造)
5. [サンプルコードから学ぶ](#サンプルコードから学ぶ)
6. [ドット絵アニメーションを作成](#ドット絵アニメーションを作成)
7. [キャラクターを動かす](#キャラクターを動かす)
8. [画面遷移を実装する](#画面遷移を実装する)
9. [Web上でPyxelアプリを実行する](#Web上でPyxelアプリを実行する)
10. [SNSへの共有機能を実装する](#SNSへの共有機能を実装する)
<!-- 各チャプター -->
<a id="#pyxelとは"></a>
# Pyxelとは
![pyxel_300000_downloads](https://user-images.githubusercontent.com/101140119/200431256-ad021bf0-dfc4-4367-816d-5128edecf07a.gif)
Pyxel(ピクセル)は，Python向けのオープンソースゲームエンジンです．
使える色は 16 色のみ，同時に再生できる音は 4 音までなど，レトロゲーム機を意識したシンプルな仕様で，Pythonでドット絵スタイルのゲームづくりが気軽に楽しめます．
限られた機能や仕様によって，初学者でも学びやすいことも一つの特徴です．

>仕様
Windows、Mac、Linux、Web で動作
Python によるプログラミング
16 色パレット
256x256 サイズ、3 画像バンク
256x256 サイズ、8 タイルマップ
4 音同時再生、定義可能な 64 サウンド
任意のサウンドを組み合わせ可能な 8 ミュージック
キーボード、マウス、ゲームパッド
画像・サウンド編集ツール

<a id="#制作したゲーム"></a>
# 制作したゲーム
![game_play](https://user-images.githubusercontent.com/101140119/200431412-646c8304-8c28-4711-9a98-f2b71a1dd414.gif)

https://github.com/rwatanab1999/Pyxel_trick_or_track

ゲームの内容を説明すると，お化けに捕まらずにどれだけお菓子を集められるか，という非常にシンプルなものです．集めたお菓子の数が増えると新たに異なる特徴のお化けが登場し，最大で4体のお化けに追いかけられます．現代っ子には見向きもされないようなゲーム性ですが，シンプルながらそこそこの難易度に調整しています．

この作品は，所属する42Tokyo学内で行われた，自由な解釈で「ホラー」なコードで競い合うHalloween Horror Code大会に合わせて制作しました．締切まで約3日間という限られた時間だったので，簡単に作れそうなテーマはないかなあと探していた際に，たまたまPyxelを見つけ採用しました．
「簡単に制作できる」というのが特徴のPyxelですが，もう一つ「他人に共有しやすい」という大きな特徴もあります．その代表として，GitHub上にソースを置くだけで，Webブラウザからアプリを直接起動できるという機能が挙げられます．専用リンクさえ知っていれば，環境構築もせず誰でもスマホから遊べるという恐ろしく素敵な機能ですよね．．．
以下のリンクから実際にこのゲームをプレイできるので，良ければお試しください．

https://kitao.github.io/pyxel/wasm/launcher/?play=rwatanab1999.Pyxel_trick_or_track.trick_or_track

それでは，学んだことや役に立った知識・文献をまとめていきます．

<a id="#環境構築とマニュアル"></a>
# 環境構築とマニュアル
Python3 (バージョン 3.7 以上) がインストールされている環境下で，次のコマンドの実行で簡単にインストールできます．Pythonパッケージとして，たった1コマンドで導入完了です．
```言語名:Windows
pip install -U pyxel
```
```言語名:Mac
pip3 install -U pyxel
```
詳細な仕様や使用方法については，リファレンスをご確認ください．
制作途中でわからないことも，ググる前にじっくりこちらを参照すると大体解決します．
https://github.com/kitao/pyxel/blob/main/docs/README.ja.md



<a id="#プログラムの基本構造"></a>
# プログラムの基本構造
リファレンスでも解説されていますが，
基本的にはPythonスクリプト内では，大きく4つの役割に分けてコードを記述します．
・ 初期化
・ フレームの更新処理
・ 描画処理
・ アプリケーションの実行
```
import pyxel # Pyxelモジュールをインポート

pyxel.init(160, 120) # 初期化(ウィンドウサイズを指定)

def update(): # フレームの更新処理
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw(): # 描画処理
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, 11)

pyxel.run(update, draw)　# アプリケーションの実行
```
上のサンプルコードでは，
はじめにinit関数でウィンドウサイズを指定した後，フレーム更新処理を行うupdate関数と描画処理を行うdraw関数を，run関数の引数に指定してアプリケーションを実行しています．
しかし，複雑な処理を行わせるゲームの制作においては，あまり向かない記述方法です．以下のようなクラス構造を用いて，Pyxelの処理をラップすることがおすすめされています．
```
import pyxel

class App:
    def __init__(self): # 初期化
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw) # アプリケーションの実行

    def update(self): # フレームの更新処理
        self.x = (self.x + 1) % pyxel.width

    def draw(self): # 描画処理
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()
```
Python自体も初心者の方向けに，ここまでに必要な「クラス」「self」「\_\_init__」あたりの知識について，参考になりそうな文献を置いておきます．コードに触れていく中で，雰囲気がわかってくるかと思います．

- [クラスと self と \_\_init__](https://python.ms/class/#はじめに)
- [Pythonのselfとかinitを理解する](https://qiita.com/ishigen/items/2d8b6e6398743f2c8110)
- [Pythonにおける__init__の利用方法を現役エンジニアが解説【初心者向け】](https://magazine.techacademy.jp/magazine/24530)

<a id="サンプルコードから学ぶ"></a>
# サンプルコードから学ぶ
初めからリファレンスや文献を読み込むよりも，実際にコードの中で機能に触れることをおすすめします．Pyxelに関しての文献がそもそも少ないので，実装されていそうなコードの中から探す機会もあるかと思います．

まずは公式が提供するサンプルコードをダウンロードしてみましょう．
Pyxel のインストール後に、次のコマンドでカレントディレクトリに Pyxel のサンプルコードがコピーされます。
```
pyxel copy_examples
```
 14 個のサンプルコードが手に入りますが，初学者に向けたものとしてはとりあえず
「01_hello_pyxel.py」「03_draw_api_py」の 2 つのみで十分かと思います．
前者では，前章のプログラムの基本構成と pyxel.frame_count の役割を理解し，
後者では，基本的な描画APIをリファレンスを見ながら確認できれば十分です．


<a id="#ドット絵アニメーションを作成"></a>
# ドット絵アニメーションを作成
<img width="953" alt="68747470733a2f2f71696974612d696d6167652d73746f72652e73332e61702d6e6f727468656173742d312e616d617a6f6e6177732e636f6d2f302f323935323432382f62326362623230622d396636622d363732642d373138312d3238646563643139396130382e706e67" src="https://user-images.githubusercontent.com/101140119/200431750-0c79340e-cab9-4ac9-b1e2-6addba53f630.png">
Pyxelには，アプリケーションで使用する画像やサウンドを作成・編集できるリソースエディタが付属しています．GUI上で簡単に操作することができ，どうぶつの森のマイデザインのような感覚でデザインすることができます．
ここまで学習した知識を使って，実際にこのようなアニメーションを作成しました．ちょろちょろ動いていて，めっちゃ可愛くないですか？？？

![pyxel-20221029-041346](https://user-images.githubusercontent.com/101140119/200431873-ff4edc87-a43c-4e00-aa27-c0b6133f71df.gif)

<a id="#キャラクターを動かす"></a>
# キャラクターを動かす
次に，キャラクターを自由に動かすプログラムを実装しました．
キーボードの十字キーの入力に応じて，キャラクターの座標変数を増減させるといったものです．入力が行われた際に，updateで増減させるだけですが，障害物や壁への当たり判定を考慮して実装する必要があります．
以下のサイトでは，移動機能の基本から順にステップアップで解説されています．
- [【Python】Pyxelで簡単な迷路ゲームを作る](https://qiita.com/hiro_underclass/items/81464fb52e6d7504d14c)．

さらに，ここでちょっとした応用として，キャラクターの座標に応じて敵(お化け)が追いかけてくる機能も実装しました．敵の移動の仕方にもよりますが，キャラクターを中心座標とした時に，相対的にどこにいるか(上下左右など)によって，場合分けして各成分の変量を決めてあげると良いです．斜めの移動に関しては，基本的なベクトルの概念の理解も必要になるかと思います．


<a id="#画面遷移を実装する"></a>
# 画面遷移を実装する
これを習得することで，複数のステージや画面を行き来することができます．
簡単な実装方法としては，まず，各画面に対して0,1,2・・・のように定数を割り当て，現在の画面を表す変数(scene)を用意します．次に，画面遷移のトリガーとなる各イベント時に(例えば何かのキーが押されたときに)，次の画面に対応する定数をsceneに代入します．最後に，updateメソッドの中でscene変数の値によって画面処理を切り替えてあげれば，画面遷移が実装できます．切り替える画面が増えれば記述量も当然増えるため，各画面の更新処理用のメソッドを用意してあげると良いかと思います．
詳しくは，以下のサイトを参考に実装してみて下さい．
- [Pyxelで作る08 画面遷移](https://mekatamatama.hatenablog.com/entry/2020/10/25/120106)

ここまでで，押さえておくべき基本事項は以上です．
あとは，欲しい機能を個別に調べて，ここまでの土台に付け足していくイメージで実装できるかと思います．
発展内容として，フラグと状態遷移の考え方はこちらで学びました．ジャンプなどのアクション動作を実装する際に，おそらく必要になってくるものです．参考にしてみてください．
- [【Pyxel】Pyxelで学ぶゲームプログラム 〜フラグと状態遷移](https://note.com/syun77/n/na69bf28eea04)

<a id="#Web上でPyxelアプリを実行する"></a>
# Web上でPyxelアプリを実行する
ちらっと先述しましたが，Pyxelには画期的な機能があります．それは，GitHub上にソースを置くだけで，Webブラウザからアプリを直接起動できるという機能です．
アプリを作ったら，やはり他の人に遊んでもらいたいものですよね．この機能の素晴らしいところは，リンクさえ知っていれば環境構築も必要なく遊べるところです．みんなにどんどん共有しましょう．
詳しくですが，Pyxelのコードやアプリ(.pyxapp)をGitHubに置いている場合、HTMLファイルの作成すら行わず、Pyxel Web LauncherのURLにファイルの置き場を指定するだけで動かすことができます。
Pyxel Web LauncherでPyxelアプリを起動する場合の書式は以下の通りです。
```
https://kitao.github.io/pyxel/wasm/launcher/?play=<githubのユーザー名>.<リポジトリ名>.<アプリのディレクトリ>.<拡張子を取ったアプリ名>
```

例えば、私の作ったアプリですと，
・ユーザー名が，rwatanab1999
・リポジトリ名が，Pyxel_trick_or_track
・アプリのディレクトリが，trick_or_track
・アプリ名が，trick_or_track
なので、

```
https://kitao.github.io/pyxel/wasm/launcher/?run=rwatanab1999.Pyxel_trick_or_track.trick_or_track
```

以上がURLになります。以下が該当のリンク先です．

https://kitao.github.io/pyxel/wasm/launcher/?play=rwatanab1999.Pyxel_trick_or_track.trick_or_track

<a id="#SNSへの共有機能を実装する"></a>
# SNSへの共有機能を実装する
Web上でアプリを動かせるようになったら，次はSNSへの共有機能も実装したいところです．
今回私が実装した機能は，ワンタッチでゲームのスコアをTwitterでツイートするという機能です．スコアの共有だけでなく，そのツイートを見た他のユーザーにリンクを踏んでもらえるような工夫も施しています．
WordleなどのWebアプリがバズった一つの要因として，SNSへの共有機能が挙げられると思います．Pyxelアプリをリリースするにあたっては，押さえておきたい機能だと思います．

では初めに，アプリ内に外部URLを設置する方法から解説します．
ブラウザを制御してWebサイトを表示するためには，Python標準組み込みモジュールのwebbrowserを使用します．標準の組込みモジュールなので新たにモジュールをインストールする必要はありません．openメソッドを用いて任意のURLを指定してあげると，ブラウザで開くことができます．
```
import webbrowser

webbrowser.open(url)
```
例えば，以下のように条件を設定してあげると，特定の範囲でマウスをクリックしたらブラウザを開くなんてことができます．
```
#42Tokyoのアイコン(16×16)
pyxel.blt(140, 108, 2, 48, 0, 16, 16, 0)

if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (140 <= pyxel.mouse_x <= 156) and (108 <= pyxel.mouse_y <= 124):
    webbrowser.open("https://42tokyo.jp")
```

<img width="70%" src=https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2952428/91269016-5f29-23e6-e2de-a1dc13a59f54.gif>

webbrowserモジュールの詳細については，以下のサイトで詳しく解説されています．
- [【Python】ブラウザを起動しWebサイトを表示する方法（webbrowserモジュール）](https://hibiki-press.tech/python/webbrowser_module/1884)

次に，ツイート機能の実装についてです．
先ほどのようにアイコンをクリックすると，定型文が自動でツイートされるというものですが，webbrowserモジュールのちょっとした応用でしかありません．ツイートさせたい定型文をツールを用いてURLエンコードし，それをopenメソッドに指定してあげるというものです．
まずは，以下のサイトでツイートリンクを生成し実際に開いてみましょう．
- [ツイートリンク生成ツール](https://tools.ikunaga.net/tweet-link/)
<img width="770" alt="スクリーンショット 2022-11-05 13 35 31" src="https://user-images.githubusercontent.com/101140119/200432058-12aa015e-8e2c-4321-a94c-3e8ebb5cfa9f.png">
<img width="587" alt="スクリーンショット 2022-11-05 13 36 00" src="https://user-images.githubusercontent.com/101140119/200432078-b287243e-6075-4223-a90e-a1231ad2ea02.png">
ここまでで，定型文のツイート機能は実装できました．
しかし，今回のアプリでは変数であるスコアを扱うため，スコアの値に応じてツイートの定型文の一部を書き換える必要があります．もちろんですが，0点から満点までそれぞれ定型文を生成するわけにはいきません．スコアが確定した時点で，雛形にスコアの値を代入してリンクを作成しましょう．

ツイートリンクの生成ですが，URLエンコードしても英数字部分の表示はそのままなので，仮のスコア部分を目印に変数を代入します
<img width="559" alt="スクリーンショット 2022-11-05 14 00 02" src="https://user-images.githubusercontent.com/101140119/200432171-fa415f8b-2950-47ed-8117-fa3b2d00df1d.png">
例えば，上の写真のように仮のリンクを生成したら，スコア部分を中括弧{}に置き換えます．
```
https://twitter.com/intent/tweet?text=score%E3%81%AF{}%E7%82%B9%E3%81%A7%E3%81%97%E3%81%9F%EF%BC%8E
```
この雛形リンクを文字列として扱うと，中括弧で置換フィールドを設定することができるformatメソッドで，スコアの値を埋め込むことができます．
```
template_link = "https://twitter.com/intent/tweet?text=score%E3%81%AF{}%E7%82%B9%E3%81%A7%E3%81%97%E3%81%9F%EF%BC%8E"
result_score = xxxx #スコアの変数
form_link = template_link.format(result_score)
webbrowser.open(form_link)
```
文字列への埋め込みには様々な形式があるので，こちらを参考にしてみてください．
- [文字列への埋め込み](https://www.python.ambitious-engineer.com/archives/422)

# おわりに
駄文長文にお付き合いいただき，ありがとうございました．
短い期間での開発でしたが，Pyxelへの様々な可能性を感じたとともに，より高度なテクニックや技術を用いて制作を継続したいと感じました．今回はBGMや効果音を作らなかったため，音楽周りのことについても今後学習しようと思います．
Pyxelは，もっと広く認知されていくポテンシャルを秘めているので，皆さんもぜひ先駆者として開発に挑戦してみてください．

