# YouTubeチャンネル状態管理ツール

channel = {
    "name": "塀の中でもバズりたい",
    "status": "運営中",
    "videos": 0,
    "subscribers": 0,
    "goal": "バズるチャンネルを作る"
}

print("📺 YouTube Channel Status")
print("-" * 30)

print(f"チャンネル名: {channel['name']}")
print(f"状態: {channel['status']}")
print(f"動画数: {channel['videos']}")
print(f"登録者数: {channel['subscribers']}")
print(f"目標: {channel['goal']}")

print("-" * 30)
print("ステータス確認完了")
