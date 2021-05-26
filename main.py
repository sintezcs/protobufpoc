from faker import Faker

from events import ProtobufCompressor


def get_some_fake_events(events_count=10):
    f = Faker()
    for _ in range(events_count):
        yield {
            'actor': f.random_digit_not_null(),
            'verb': f.random_element(['tweet', 'sms', 'other']),
            'object': f.random_digit_not_null(),
            'target': None,
            'time': f.date(),
            'foreign_id': None,
            'id': f.uuid4(),
            'tweet': f.text(160)
        }


if __name__ == '__main__':
    pc = ProtobufCompressor()
    events = [pc.compress(evt) for evt in get_some_fake_events(5000)]
    pc.print_and_reset_stats()
