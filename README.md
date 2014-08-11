tinker2pelican-rst
===========================

[Tinkerer](http://tinkerer.me) から [Pelican](https://github.com/getpelican/pelican) に移行する際に、
ReSTの方言を修正して、画像ファイルを移動するスクリプトです。


Description
-------------------------------------

作者が実際に移行するためにかなりやっつけで作ったため、本当に最低限の事しかできないです。  

スクリプトを実行する際のカレントディレクトリ配下でファイルパスが `content/201*/MM/DD/<filename>.rst` に該当するもの全てに対して以下の書き込みをします。**移動ではなく直接変換処理を行うのでご注意を**

* `author` ディレクティブを削除
* `categories`, `tags`, `comments` ディレクティブをオプションに変更し、ファイル3行目のところまで移動
* `.. more::` ディレクティブを `.. PELICAN_END_SUMMARY` に変換。
* 画像ファイルのパスと配置を修正
    * `.. image:: hoge.png` => `..image:: /images/YYYY/MM/DD/hoge.png` に変換
    * `content/YYYY/MM/DD` 配下にpng, jpg ファイルがある場合は `images/YYYY/MM/DD` 配下に移動

Requirement
----------------------
### スクリプトの動作環境

以下の環境で動作の確認が取れています。

* python 2.7.8

### 変換後のpelicanの設定

* 変換後のReSTファイルは `summary` プラグインが必要
* 画像ファイルを `/path/to/pelican/content/images/YYYY/MM/DD` 配下に移動するので `STATIC_PATH` の設定が必要

### 手順

* pluginの導入

    ```sh
    % cd /path/to/pelican
    % git clone https://github.com/getpelican/pelican-plugins.git

    % vim pelicanconf.py
    ```

* `pelicanconf.py` 追記内容

    ```python
    ## 画像ファイル向け
    STATIC_PATHS = [ ..., 'images', ]
    EXTRA_PATH_METADATA = { 'images': { 'path': 'images' } }

    ## プラグイン追加
    PLUGIN_PATHS = [ 'pelican-plugins' ]
    PLUGINS = [ ..., 'summary' ]
    ```

Usage
----------------------

```sh

% cd /path/to/pelican
% cp -R /path/to/tinkerer/201* content/

% python tinker2pelican.py

```
