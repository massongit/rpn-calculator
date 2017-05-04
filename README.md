# rpn-calculator
CLIによるRPN電卓

##動作環境
* Python 3.6.0
* Python 2.7.13

##インストール方法
1. `six`を導入します。
   * Ubuntuの場合  
     `sudo apt python-six`
   * それ以外の場合  
     `pip install six`
1. `echo "alias rpn='python {rpn.pyのフルパス}'" >> ~/.bashrc`コマンドを実行し、`rpn`コマンドを追加します。
1. `source ~/.bashrc`コマンドを実行し、変更を適用します。

##対応している演算

|演算子|内容|
|:---:|:---:|
|`+`|加算|
|`-`|減算|
|`*`|乗算|
|`/`|除算|
|`%`|剰余|
|`^`|冪乗|

## 使用例
`10 * 5 + 2`の場合
```
$ python rpn.py
> 10  
10.0
> 5*
5.0
50.0
> 2+
2.0
52.0
>
```

## ライセンス
Copyright (c) 2017 Masaya SUZUKI <<suzukimasaya428@gmail.com>>

Released under the [MIT license](LICENSE.txt)
