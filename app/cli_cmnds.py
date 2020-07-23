import click
from flask.cli import with_appcontext
import traceback
from app.ssp_module.models import init_db
from app.app import create_app

app = create_app()
app.cli.add_command(new_site)


@click.command(name="new-site", help="create new database")
@click.argument("name")
@with_appcontext
def new_site(name):
	try:pass
		# init_db()
	except Exception as e:
		traceback.print_exc(limit=1, file=sys.stdout)
