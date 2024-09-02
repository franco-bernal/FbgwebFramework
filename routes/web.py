# routes/web.py
from fbgrouter.classes.router import Router
from controllers.home_controller import home
from controllers.help_controller import help
from controllers.chat_a_controller import chata
from controllers.chat_b_controller import chatb

# Configuración de rutas
router = Router()
router.add_route("/", home, method='GET')
router.add_route("/help", help, method='GET')
router.add_route("/chata", chata, method='GET')
router.add_route("/chatb", chatb, method='GET')
