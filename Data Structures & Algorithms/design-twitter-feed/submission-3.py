from heapq import heapify, heappush, heappop

class Twitter:

    def __init__(self):
        self.follows = {}
        self.threads = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        entry = (self.time, tweetId)

        if userId in self.threads:
            self.threads[userId].append(entry)
        else:
            self.threads[userId] = [entry]
        
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follows.get(userId, set())
        threads = [self.threads.get(id, []) for id in followees]
        
        heap = []
        for i in range(len(threads)):
            if not threads[i]: continue
            ts, val = threads[i][-1]
            t_id = i
            e_id = len(threads[i]) - 1

            heap.append((-ts, val, t_id, e_id))
        heapify(heap)

        result = []
        while heap and len(result) < 10:
            _, val, t_id, e_id = heappop(heap)
            result.append(val)

            if e_id - 1 >= 0:
                ts, val = threads[t_id][e_id - 1]
                t_id = t_id
                e_id = e_id - 1
                heappush(heap, (-ts, val, t_id, e_id))
        
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
