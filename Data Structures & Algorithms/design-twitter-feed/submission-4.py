class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweets[userId].append((self.counter, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        required_users = list(self.followers[userId]) + [userId]
        result = []

        for user in required_users:
            user_tweets = self.tweets[user][-1:-11:-1]
            if not user_tweets:
                continue
            l = 0
            r = 0
            nr = []
            while l<len(result) and r< len(user_tweets):
                if result[l][0] < user_tweets[r][0]:
                    nr.append(user_tweets[r])
                    r+=1
                else:   
                    nr.append(result[l])
                    l+=1
            while len(nr) < 10 and l < len(result):
                nr.append(result[l])
                l+=1
            while len(nr) < 10 and r < len(user_tweets):
                nr.append(user_tweets[r])
                r+=1
            result = nr[:10]
        return [i[1] for i in result]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)