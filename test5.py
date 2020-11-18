def producer(queue, start, end, step):
    for value in range(start, end, step):
        queue.put(value)
    print('Producer finished')


def consumer(queue, count, result, lock):
    local_result = []
    for _ in range(count):
        local_result.append(queue.get())
    with lock:
        result.update(local_result)
    print('Consumer finished')


def main():
    value_count = 500000
    producer_count = 50
    consumer_count = 50
    assert value_count % producer_count == 0
    assert value_count % consumer_count == 0

    queue = Queue(123)
    result = set()
    lock = Lock()
    producers = [Thread(target=producer, args=(queue, i, value_count, producer_count)) for i in range(producer_count)]
    consumers = [Thread(target=consumer, args=(queue, value_count // consumer_count, result, lock)) for _ in range(consumer_count)]

    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    for p in producers:
        p.join()
    for c in consumers:
        c.join()

    if len(result) != value_count:
        raise ValueError('Result size is %d instead of %d' % (len(result), value_count))


if __name__ == '__main__':
    main()