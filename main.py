import json
from pathlib import Path
from errors import AppError , ConfigError , ConfigFileMissingError , InvalidConfigError


config_path = Path("config.json")

try:
    if not config_path.exists():
          raise ConfigFileMissingError("config.json not found")
    
    f = open(config_path)
    config = json.load(f)
    f.close()
    print(config)


except ConfigFileMissingError as e:
    print(e)
except InvalidConfigError as e:
     print(e)






