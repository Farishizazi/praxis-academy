from json_checker import Checker

def TesCre(request):
    try:
        schema = {
            "title": str,
            "description": str
        }
        checker = Checker(schema)
        checker.validate(request)
        return False 
    except Exception as err:
        return err

def TesUp(data):
    try:
        checker = Checker({
            "title": str,
            "description": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err