from flask import Blueprint


main_module = Blueprint(
	'main_module',
	__name__,
	template_folder='main_module-templates',
	static_folder='main_module-static'
)

from . import views