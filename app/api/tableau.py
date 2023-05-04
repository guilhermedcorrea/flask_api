from flask import Blueprint
from flask import jsonify, make_response, request



TABLEAU = Blueprint("tableau",__name__)


@TABLEAU.route("/tableau")
def get_user_tableau():
    return "usertableau"