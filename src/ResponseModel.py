def ResponseModel(data, message):
    if type(data) is list:
        return {
            "data": data,
            "code": 200,
            "message": message,
        }
    else:
        return {
            "data": [data],
            "code": 200,
            "message": message,
        }