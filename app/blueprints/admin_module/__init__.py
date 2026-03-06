from flask import Blueprint


admin_module = Blueprint(
	'admin_module',
	__name__,
	template_folder='admin_module-templates',
	static_folder='admin_module-static'
)

from . import views