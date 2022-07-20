import json

INVALID_PARAMETER_VALUE = 'Input validation error - invalid parameter value'
SERVER_ERROR = 'Server error'


def response_200(body: ...) -> dict[str, ...]:
    """Send 200 response."""
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }


def response_400() -> dict[str, ...]:
    return {
        'statusCode': 400,
        'body': INVALID_PARAMETER_VALUE
    }


def response_500() -> dict[str, ...]:
    return {
        'statusCode': 500,
        'body': SERVER_ERROR
    }
