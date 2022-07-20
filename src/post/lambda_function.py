import logging

from data_handler import DataHandler, ValidationError, ClientError
import response

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SUCESS_STATUS = 'Item created'


def lambda_handler(event, context):
    logger.info('## EVENT')
    logger.info(event)
    try:
        DataHandler().post(event)
    except ValidationError as e:
        logging.error(e)
        return response.response_400()
    except ClientError as e:
        logging.error(e)
        return response.response_500()

    return response.response_200(SUCESS_STATUS)
