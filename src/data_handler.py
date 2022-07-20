import boto3
from botocore.exceptions import ClientError
import logging
from pydantic import ValidationError
from typing import List

from model import Announcement

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DataHandler:
    """Process HTTP request using boto3."""

    TABLE_NAME = 'announcement'

    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.resource = boto3.resource('dynamodb')

    def get(self, limit: int, offset: int) -> List[Announcement]:
        """Get announcement records from database."""
        paginator = self.client.get_paginator('scan')
        items = []
        for num, page in enumerate(paginator.paginate(
                TableName=self.TABLE_NAME,
                PaginationConfig={'PageSize': limit})):
            if num + 1 == offset:
                for item in page['Items']:
                    items.append({key: value.get('S') for key, value in item.items()})
                break

        logging.info('%s items are retrieved', len(items))
        return items

    def post(self, event: dict[str, str]):
        """Create an announcement in database."""
        announcement = Announcement(**event).dict()
        table = self.resource.Table(self.TABLE_NAME)
        table.put_item(Item=announcement)
        logging.info('New item is created: %s', announcement)
