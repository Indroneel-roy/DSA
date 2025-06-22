# Problem Link : https://leetcode.com/problems/design-twitter/description/
import heapq
from collections import defaultdict
from typing import List
import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        # Counter to simulate time (newer tweets have smaller count)
        self.count = 0
        # Map userId -> list of [count, tweetId]
        self.tweetmap = defaultdict(list)
        # Map userId -> set of followees
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # User always follows themselves
        self.followmap[userId].add(userId)

        # Add latest tweet from each followee to the heap
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId]) - 1
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # Get up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)

if __name__ == "__main__":
    twitter = Twitter()

    twitter.postTweet(1, 101)  # User 1 posts tweet 101
    twitter.postTweet(1, 102)  # User 1 posts tweet 102

    twitter.follow(2, 1)       # User 2 follows User 1

    print(twitter.getNewsFeed(2))  # Output: [102, 101]

    twitter.postTweet(2, 201)  # User 2 posts tweet 201
    print(twitter.getNewsFeed(2))  # Output: [201, 102, 101]

    twitter.unfollow(2, 1)     # User 2 unfollows User 1
    print(twitter.getNewsFeed(2))  # Output: [201]
