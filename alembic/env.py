import logging
from logging.config import fileConfig
from alembic import context
from app import create_app  # Substitua pelo caminho correto da sua função de criação de app

# Criação da instância do aplicativo
app = create_app()

# Configuração do logging
config = context.config
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

def get_engine():
    # Certifique-se de que estamos no contexto da aplicação
    with app.app_context():
        return app.extensions['migrate'].db.get_engine()

def get_engine_url():
    with app.app_context():
        return get_engine().url.render_as_string(hide_password=False).replace('%', '%%')

# Adiciona o MetaData do modelo aqui
config.set_main_option('sqlalchemy.url', get_engine_url())
target_db = app.extensions['migrate'].db

def get_metadata():
    if hasattr(target_db, 'metadatas'):
        return target_db.metadatas[None]
    return target_db.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=get_metadata(), literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    conf_args = app.extensions['migrate'].configure_args
    if conf_args.get("process_revision_directives") is None:
        conf_args["process_revision_directives"] = process_revision_directives

    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=get_metadata(), **conf_args)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
