from flask import Blueprint,abort,make_response
from ..models.cat import cats


# Definig the Bp (above) and instantiate it here
cats_bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

#making routes
@cats_bp.get("")
def get_all_cats():
   
    results_list = []

    for cat in cats:
        results_list.append(dict(
            id=cat.id, 
            name=cat.name, 
            color=cat.color, 
            personality=cat.personality
            ))

    return results_list

@cats_bp.get("/<cat_id>")
def get_one_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        return {"message":f"Cat id {cat_id} invalid"}, 400
    # cat_id = int(cat_id)

    for cat in cats:
        if cat.id == cat_id:
            return dict(
            id=cat.id, 
            name=cat.name, 
            color=cat.color, 
            personality=cat.personality
            )
        
    return {"message" : f"cat {cat_id} not found "}, 404

# def validate_cat(cat_id):
#     try:
#         cat_id = int(cat_id)
#     except:
#         abort(make_response({"message":f"Cat id {cat_id} invalid"}, 400))

    # for cat in cats:
    #     if cat.id == cat_id:
    #         return cat
        

    # abort(make_response({"message":f"Cat id {cat_id} invalid"}, 404))
        
  
    

    
        

    


