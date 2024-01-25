import environ

# Extracts secrets from Vault-via-envconsul: 'secret/your-app':
vault = environ.secrets.VaultEnvSecrets(vault_prefix="SECRET_YOUR_APP")

@environ.config(prefix="APP")
class AppConfig:
    @environ.config
    class DB:
        name = environ.var("default_db")
        host = environ.var("localhost")
        port = environ.var(5432, converter=int)  # Use attrs's converters and validators!
        user = environ.var("default_user")
        password = vault.secret()

    env = environ.var()
    lang = environ.var(name="LANG")  # It's possible to overwrite the names of variables.
    db = environ.group(DB)
    awesome = environ.bool_var()

# Set environment variables for configuration
environ.Env.read_env()
cfg = environ.to_config(
    AppConfig,
    environ={
        "APP_ENV": "dev",
        "APP_DB_HOST": "localhost",
        "LANG": "C",
        "APP_AWESOME": "yes",  # true and 1 work too, everything else is False
        # Vault-via-envconsul-style var name:
        "SECRET_YOUR_APP_DB_PASSWORD": "s3kr3t",
    }
)

# Print the AppConfig instance
print(cfg)
# Output: AppConfig(env='dev', lang='C', db=AppConfig.DB(name='default_db', host='localhost', port=5432, user='default_user', password=<SECRET>), awesome=True)

# Access the password attribute of the db attribute of the AppConfig instance
print(cfg.db.password)
# Output: 's3kr3t'
