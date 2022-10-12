from flask import request
from todo import validators
from todo import responses
from http import HTTPStatus
from todo import models

def Create():
    bodyJson = request.json
    err = validators.TesCre(bodyJson)
    if err:
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.value,
            Message="error",
            Data=str(err)
        )
    
    collTable = models.Tables(title=bodyJson["title"], description=bodyJson["description"])
    collTable.save()

    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={}
    )

def List():
    collTable = models.Tables.objects().all()
    data = []
    for i in collTable:
        data.append({
            "id": str(i.id),
            "title": i.title,
            "description": i.description,
        })
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=data
    ), HTTPStatus.OK.value

def Update(tableId):
    bodyJson = request.json
    err = validators.TesUp(bodyJson)
    if err:
        return responses.Make(
            Status=HTTPStatus.BAD_REQUEST.OK,
            Message="error",
            Data=str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collTable = models.Tables.objects(id=tableId).update(title=bodyJson["title"], description=bodyJson["description"])
    return bodyJson

def Delete(tableId):
    models.Tables.objects(id=tableId).delete()
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=f"successfully deleted table with id: {tableId}"
    ), HTTPStatus.OK.value

def Detail(tableId):
    collTable = models.Tables.objects(id=tableId).first()
    if not collTable:
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="doesn't exist."
        ), HTTPStatus.BAD_REQUEST.value
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={
            "title": collTable.title,
            "description": collTable.description
        }
    ), HTTPStatus.OK.value