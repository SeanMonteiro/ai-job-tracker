def success_response(data=None, message=None):
    return {
        "success": True,
        "data": data,
        "message": message
    }

def error_response(message=None, data=None):
    return {
        "success": False,
        "data": data,
        "message": message
    }