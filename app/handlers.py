from werkzeug.exceptions import HTTPException
from flask import abort, jsonify


def register_handlers(app):
    if app.config.get('DEBUG') is True:
        app.logger.debug('Error Handlers')
        return
 
    @app.errorhandler(403)
    def forbidden_page(e):
        return jsonify(error=str(e)), 403

    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({"erro":"eroooooooooooooo"}), 404

    
    @app.errorhandler(405)
    def method_not_allowed_page(e):
        return jsonify(error=str(e)), 405

    @app.errorhandler(500)
    def internal_server_error(e):
        
        return jsonify(error=str(e)), 500