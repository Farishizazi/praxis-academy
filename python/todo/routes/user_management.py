from todo import app
from todo.controllers import user_management

app.route("/create", methods=["POST"])(user_management.Create)
app.route("/list", methods=["GET"])(user_management.List)
app.route("/update/<tableId>", methods=["PUT"])(user_management.Update)
app.route("/delete/<tableId>", methods=["DELETE"])(user_management.Delete)
app.route("/detail/<tableId>", methods=["GET"])(user_management.Detail)