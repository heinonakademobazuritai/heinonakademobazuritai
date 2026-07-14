import os

thumbnail_folder = "thumbnails"

print("🖼️ サムネイル確認")
print("-" * 30)

if not os.path.exists(thumbnail_folder):
    print("thumbnails フォルダがありません")
    print("作成してください")
else:
    files = os.listdir(thumbnail_folder)

    if len(files) == 0:
        print("サムネイルがありません")
    else:
        for file in files:
            print(f"✅ {file}")

print("-" * 30)
print("確認完了")
