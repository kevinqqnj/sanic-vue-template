"""
REST API Resource Routing
"""

from sanic import response
from sanic.views import HTTPMethodView
from sanic.log import logger

from datetime import datetime

from .security import authorized
from . import api_bp

class SimpleAsyncView(HTTPMethodView):

    async def get(self, request):
        logger.debug(f'>>> view.get method. resource_id: {request.args.get("id")}')
        return response.json({'timestamp': datetime.utcnow().isoformat()})

    @staticmethod
    @authorized()
    async def post(self, request):
        logger.debug(f'>>> view.post method. resource_id: {request.json}')
        return response.json({'timestamp': datetime.utcnow().isoformat()})

    async def put(self, request):
        return response.text('I am async put method')

    async def delete(self, request):
        return response.text('I am delete method')

api_bp.add_route(SimpleAsyncView.as_view(), '/resource')        
