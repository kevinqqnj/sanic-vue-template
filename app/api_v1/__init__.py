""" API Blueprint Application """

from sanic import Blueprint, response
# from flask_restplus import Api
from datetime import datetime

# --> '/v1/api/'
api_bp = Blueprint('api_bp_v1', url_prefix='/api', version='v1')
# api_rest = Api(api_bp)


# @api_bp.after_request
# async def add_header(response):
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
#     return response

@api_bp.route('/')
async def bp_root(request):
    return response.json({'api_bp_v1': 'blueprint'})

@api_bp.route('/resource/<resource_id:string>')
async def resouce1(request, resource_id):
    timestamp = datetime.utcnow().isoformat()
    return response.json({'timestamp': timestamp})

# Import resources to ensure view is registered
# from .resources import * # NOQA
