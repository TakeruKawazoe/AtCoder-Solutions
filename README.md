# AtCoder-Solutions

就活に向けて、継続的なコーディング習慣を可視化するための AtCoder 解答リポジトリです。

主に以下を目的にしています。
- Python での基礎実装力の強化
- 問題を継続して解く習慣の定着
- GitHub 上での学習ログ公開

## 対象
- AtCoder Programming Guide for beginners（APG4b）
- 今後、ABC なども追加予定

## リポジトリ構成

AtCoder-Solutions/
  README.md
  .gitignore
  docs/
    upload-guide.md
  atcoder/
    apg4b/
      README.md
      answers/
        .gitkeep
    abc/
      README.md
      .gitkeep

## 解答追加ルール（統一）
- 1 問 1 ファイル
- ファイル先頭に問題 URL をコメントで記載
- 変数名は短すぎないようにする（読みやすさ重視）
- 可能なら各問題で「学んだこと」を 1 行コメントで残す

ファイル名ルール（推奨）
- APG4b: q001.py, q002.py, ...
- ABC: abc350_a.py, abc350_b.py, ...
- テンプレート: atcoder/apg4b/answers/q000_template.py

## 進め方（最小運用）
1. 問題を 1 問解く
2. 解答ファイルを追加
3. 必要に応じて 해당ディレクトリの README に 1 行メモを追記
4. コミット
5. GitHub に push

コミットメッセージ例
- apg4b: add q001
- apg4b: add q002
- abc350: add a,b

## 実行方法（ローカル）
PowerShell 例:
python .\atcoder\apg4b\answers\q001.py

## 学習ログの見せ方（就活向け）
- 連続した日付で小さく積み上げる（草を継続）
- 1 回のコミットを小さく保つ（活動内容が見えやすい）
- 難問だけでなく基礎問題の継続も含めて公開する

---
必要になったら、以下を追加予定
- テスト用スクリプト
- 解法メモ（Markdown）
- 実行時間比較の記録
