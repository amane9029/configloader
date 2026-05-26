#errors.py

class AppError(Exception):
    pass

class ConfigError(Exception):
    pass

class ConfigFileMissingError(Exception):
    pass

class InvalidConfigError(Exception):
    pass

