from flask_restplus import fields
from app import app_api

BaseError = app_api.model('BaseError', {
    'status': fields.String(required=True, description='Status'),
    'statusCode': fields.String(required=True, description='Status code')
})
