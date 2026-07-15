# YouTube投稿スケジュール管理ツール

schedule = [
    {
        "date": "2026-07-20",
        "title": "塀の中でもバズりたい理由",
        "status": "予定"
    },
    {
        "date": "2026-07-25",
        "title": "GitHubでYouTube管理してみた",
        "status": "制作中"
    }
]

print("📅 YouTube投稿スケジュール")
print("-" * 30)

for video in schedule:
    print(f"📆 日付: {video['date']}")
    print(f"🎬 タイトル: {video['title']}")
    print(f"状態: {video['status']}")
    print("-" * 30)

print("スケジュール確認完了")
