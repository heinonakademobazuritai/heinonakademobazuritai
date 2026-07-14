# YouTube投稿チェックツール

checklist = [
    "タイトル確認",
    "説明文確認",
    "サムネイル確認",
    "タグ確認",
    "公開設定確認"
]

print("📺 YouTube投稿チェック")
print("-" * 30)

for i, item in enumerate(checklist, 1):
    print(f"{i}. ⬜ {item}")

print("-" * 30)
print("投稿準備チェック完了")
