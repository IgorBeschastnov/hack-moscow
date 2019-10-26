import json
import logging
import time

from redis import Redis

from conf.settings import COLLECT_TIMEOUT

from common.redis_sync import BaseRedisSyncStorage
from common.models import CollectorLocation
from northstar.models import User, UserCategory

log = logging.getLogger(__name__)
redis = BaseRedisSyncStorage(Redis(host='localhost', port=6379, db='0'), '')
redis_cities = BaseRedisSyncStorage(Redis(host='localhost', port=6379, db='1'), '')
USER_LOCATIONS_PER_SCAN = 5


def loop():
    while True:
        try:
            log.debug('Running collection')
            collect()
        except Exception:
            log.exception('Caught exception in main collector thread!')
        time.sleep(COLLECT_TIMEOUT)


def collect():
    for key in redis:
        for _ in range(USER_LOCATIONS_PER_SCAN):
            log.info(f'Processing key {key}')
            value = redis.rpop(key)
            if not value:
                break
            process_value(key, value)


def process_value(key, value):
    try:
        location = CollectorLocation(**json.loads(value))

        redis_cities.lpush(location.city, value)

        user_query = User.objects.filter(uid=key)
        if not user_query.exists():
            user = User(uid=key)
            user.save()
        else:
            user = user_query.first()

        user_category_query = UserCategory.objects.filter(
            user=user,
            category=location.category.id,
        )
        if not user_category_query.exists():
            user_category = UserCategory(user=user, category=location.category.id)
        else:
            user_category = user_category_query.first()

        user_category.points += 1
        user_category.save()
    except Exception:
        log.exception(f'Caught exception while collecting data for user {key}')