# python-unit-test
Python の練習

# setup (Mac の場合)
`pyenv` と `pyvenv` に注意。

## Python Version Manager (pyenv) をインストール
```bash
brew install pyenv
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

## pyenv を使って Python をインストール
```bash
pyenv install 3.5.2
pyenv global 3.5.2

python -V
```

## Python package をローカルインストールするための準備
例として、ディレクトリを `your_proj` とする。

```bash
mkdir  your_proj
pyvenv your_proj
source your_proj/bin/activate
```
## テストライブラリをインストール
```bash
pip install -r requirements.txt
```

## IntelliJ 設定
- File > Project Structure > Project Settings > Project SDK > New
- bin/pythonX.X を選択

## テスト実行
単体テストのみ実行するとき
```bash
mamba spec/*
```

単体テスト + テストカバレッジ計測
```bash
./bin/run_spec.sh
```

カバレッジレポート閲覧＆カバーできていない箇所を探すとき
```bash
open coverage_report/index.html
```

## venv 解除
```bash
deactivate
```

