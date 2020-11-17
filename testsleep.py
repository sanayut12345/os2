from threading import Event

class Sleep(object):
    def __init__(self, seconds, immediate=True):
        self.seconds = seconds
        self.event = Event()
        if immediate:
            self.sleep()

    def sleep(self, seconds=None):
        if seconds is None:
            seconds = self.seconds
        self.event.clear()
        self.event.wait(timeout=seconds)

    def wake(self):
        self.event.set()

if __name__ == '__main__':
    from threading import Thread
    import time
    import logging

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(created)d - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("sleep")
    s = Sleep(3)
    logger.info("awake")

    def wake_it(sleeper):
        time.sleep(2)
        logger.info("wakeup!")
        time.sleep(10)
        sleeper.wake()

    def wait_thread(sleeper):
        sleeper.sleep()
        logger.info("Processes wait!")

    logger.info("sleeping again")
    s = Sleep(20, immediate=False)
    s2 = Sleep(60,immediate=False)
    Thread(target=wait_thread,args=[s2]).start()
    Thread(target=wake_it, args=[s]).start()
    s.sleep()
    logger.info("awake again")