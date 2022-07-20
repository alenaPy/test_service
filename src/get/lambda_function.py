import logging

from data_handler import DataHandler, ClientError
import response

logger = logging.getLogger()
logger.setLevel(logging.INFO)

DEFAULT_OFFSET = 1
DEFAULT_LIMIT = 20


def lambda_handler(event, context):
    logger.info('## EVENT')
    logger.info(event)

    limit = int(event.get('limit') or DEFAULT_LIMIT)
    offset = int(event.get('offset') or DEFAULT_OFFSET)
    logger.info(f'{limit=}, {offset=}')
    try:
        items = DataHandler().get(limit, offset)
    except ClientError as e:
        logging.error(e)
        return response.response_500()

    return response.response_200(items)
