from json_checker import Checker

def TesReg(request):
    try:
        schema = {
            "userName": str,
            "userPassword": str,
            "userEmail": str,
            "roleId": str
        }
        checker = Checker(schema)
        checker.validate(request)
        return False 
    except Exception as err:
        return err

def TesUp(data):
    try:
        checker = Checker({
            "userEmail": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err