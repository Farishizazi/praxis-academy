from flask import request
from app import validators
from app import responses
from http import HTTPStatus
from app import models
from app import configs
from hashlib import md5
from logging import error

def Register():
    bodyJson = request.json
    err = validators.TesReg(bodyJson)
    if err:
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.value,
            Message="Mission Failed",
            Data=str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collUser = models.Users(
        userName = bodyJson["userName"],
        userEmail = bodyJson["userEmail"],
        userPassword = (md5((bodyJson["userPassword"]+configs.flaskSecretKey).encode())).hexdigest(),
        roleId = bodyJson["roleId"])
    collUser.save()
    
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="Success",
        Data=f"user {bodyJson['userName']} has created"
    ), HTTPStatus.OK.value

def Login():
    try:
        bodyJson = request.json
        collUser = models.Users.objects(
            userName=bodyJson["userName"],  
            userPassword=(md5((bodyJson["userPassword"]+configs.flaskSecretKey).encode())).hexdigest()).first()
        if not collUser:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="user doesn't exist"
            ), HTTPStatus.BAD_REQUEST.value

        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="Success",
            Data={
                "userName": collUser.userName,
                "userEmail": collUser.userEmail,
                "userRole": models.Roles.objects.first().roleName # atau collUser.roleId.roleName
            }
        ), HTTPStatus.OK.value
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.value,
            Message="error",
            Data=str(err)
        ), HTTPStatus.BAD_REQUEST.value

def ListUser():
    collUser = models.Users.objects().all()
    data = []
    for i in collUser:
        data.append({
            "userId": str(i.id),
            "userName": i.userName,
            "userEmail": i.userEmail,
            "userRole": i.roleId.roleName
        })
    # print(collUser)
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=data
    ), HTTPStatus.OK.value

def UpdateUser(userId):
    bodyJson = request.json
    err = validators.TesUp(bodyJson)
    if err:
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.OK,
            Message="error",
            Data=str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collUser = models.Users.objects(id=userId).update(userEmail=bodyJson["userEmail"])
    # userId = request.args["userId"]
    return bodyJson

def DeleteUser(userId):
    models.Users.objects(id=userId).delete()
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=f"successfully deleted user with id: {userId}"
    ), HTTPStatus.OK.value

def DetailUser(userId):
    collUser = models.Users.objects(id=userId).first()
    if not collUser:
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="user doesn't exist."
        ), HTTPStatus.BAD_REQUEST.value
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={
            "userName": collUser.userName,
            "userEmail": collUser.userEmail,
            "roleId": models.Roles.objects.first().roleName
        }
    ), HTTPStatus.OK.value