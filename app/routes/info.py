from flask import Blueprint, jsonify
import socket
from app.utils.pokeneas import get_random_pokenea

info_bp = Blueprint('info', __name__)

@info_bp.route('/pokenea-info', methods=['GET'])
def pokenea_info():
    pokenea = get_random_pokenea()
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": socket.gethostname()
    })