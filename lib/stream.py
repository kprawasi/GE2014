class CustomStreamListener(tweepy.StreamListener):
    def __init__(self):
        super(CustomStreamListener,self).__init__()
self.pool = Pool(5)

def on_status(self, status):
    # this is where a worker thread pool will be handed over the tasks of computing and updating the tables instead of two print stmts
    print 'status is' + str(status.text) + 'status id is ' + str(status.id) + 'string Id is '+ str(status.id_str) + 'number of followers ' + str(status.author.followers_count)
# rt_status is another Status object that holds details about the retweeted status
rt_status = status.retweeted_status
print 'status is' + str(rt_status.text) + 'status id is ' + str(rt_status.id) + 'string Id is '+ str(rt_status.id_str) + 'number of followers ' + str(rt_status.author.followers_count)
self.f(status)

def on_timeout(self):
    return True

def on_error(self, status_code):
    return True
def f(self,st):
    self.pool.apply_async(global_f, st)

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['#zyx'])
