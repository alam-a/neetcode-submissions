class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets[userId].append((-self.counter, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        required_users = list(self.followers[userId]) + [userId]

        import heapq
        result = []
        for user in required_users:
            user_tweets = self.tweets[user][-10:]
            for tweet in user_tweets:
                if len(result) >= 9:
                    heapq.heappushpop(result, tweet)
                else:
                    heapq.heappush(result, tweet)
        result.sort()
        return [user_tweet[1] for user_tweet in result]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)

    # ["Twitter", "postTweet", [1, 100], "follow", [1, 1], "getNewsFeed", [1], "unfollow", [1, 1], "getNewsFeed", [1]]
    # [null,null,null,[100,100],null,[100]]
    # ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
