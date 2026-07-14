# YouTube Analytics メモツール

videos = [
    {
        "title": "塀の中でもバズりたい",
        "views": 0,
        "likes": 0
    },
    {
        "title": "GitHubでYouTube管理してみた",
        "views": 0,
        "likes": 0
    }
]

print("📊 YouTube Analytics")
print("-" * 30)

for video in videos:
    print(f"🎬 {video['title']}")
    print(f"再生数: {video['views']}")
    print(f"高評価: {video['likes']}")
    print("-" * 30)

print("分析メモ完了")
