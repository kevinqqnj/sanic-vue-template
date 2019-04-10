""" API Blueprint Application """

from sanic import Blueprint, response
from sanic.log import logger

from datetime import datetime

# --> '/api/v1/'
api_bp = Blueprint('api_bp_v1', url_prefix='/api/v1')

# @api_bp.route('/')
# async def bp_root(request):
#     return response.json({'api_bp_v1 blueprint': 'root'})

# Import resources to ensure view is registered
from .resources import *
