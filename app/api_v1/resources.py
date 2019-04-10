"""
REST API Resource Routing
"""

from sanic import response
from sanic.log import logger

from datetime import datetime

from .security import authorized
from . import api_bp


@api_bp.route('/resource/<resource_id:string>')
async def resouce(request, resource_id):
    timestamp = datetime.utcnow().isoformat()
    logger.debug(f'resource_id: {resource_id}')
    return response.json({'timestamp': timestamp})


@api_bp.route('/resource_sec/<resource_id:string>')
@authorized()
async def resouce_secure(request, resource_id):
    timestamp = datetime.utcnow().isoformat()
    logger.debug(f'secured resource_id: {resource_id}')
    return response.json({'timestamp': timestamp})
