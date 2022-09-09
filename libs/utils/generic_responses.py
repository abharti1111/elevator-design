from libs.config import Config


def generate_success_response(data=None, msg=Config.GENERIC.SUCCESS, upfront_heads=None, sidebar_heads=None):
    response = {"status": msg[0], "message": msg[1], "data": data}
    if upfront_heads or sidebar_heads:
        response['upfront_heads'] = upfront_heads or {}
        response['sidebar_heads'] = sidebar_heads or {}
    return response