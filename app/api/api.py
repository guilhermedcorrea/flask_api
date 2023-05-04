from flask import Blueprint,current_app
from flask import jsonify, make_response, request, abort
import uuid
from flask_smorest import abort


API = Blueprint('api',__name__)

stores = {}
items = {}




@API.route("/store")
def get_stores():
    try:
        return {"stores":list(stores.values())}
    except:
        abort(404, description="url invalidaaaaaaa not found")
        
@API.route("/store", methods=['GET','POST'])
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(404, message="Error. 'price', 'store_id', and 'name' not fouund " )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            abort(404, message="Error. 'price', 'store_id', and 'name' not fouund " )
            
    store_id = uuid.uuid4().hex
    store = {**store_data,"id":store_id}
    stores[store_id] = store
    return store, 201


@API.route("/item")
def create_item():
    item_data = request.get_json()
    
    if "price" not in item_data or "store_id" not in item_data or "name" not in item_data:
    
        abort(404, message="Error. 'price', 'store_id', and 'name' not fouund " )

    for item in item.values(): 
        if item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]:
        
            abort(404, message="Error. 'price', 'store_id', and 'name' not fouund " )
            
        if item_data["store_id"] not in stores:
            abort(404, message="Error. 'price', 'store_id', and 'name' not fouund " )
        
    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    items[item_id] = item
    return item, 201
    
    
@API.route("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return abort(404, message="Error. 'price', 'store_id', and 'name' not fouund " )
