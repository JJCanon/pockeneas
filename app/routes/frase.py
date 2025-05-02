from flask import Blueprint, render_template
import socket
from app.utils.pokeneas import get_random_pokenea

frase_bp = Blueprint('frase', __name__)

@frase_bp.route('/pokenea-frase', methods=['GET'])
def pokenea_frase():
    pokenea = get_random_pokenea()
    return render_template('frase.html',
                           imagen_url=pokenea["imagen"],
                           frase=pokenea["frase"],
                           contenedor_id=socket.gethostname())