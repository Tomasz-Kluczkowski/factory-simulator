class ConfigError(Exception):
    def __init__(self, msg, *args):
        super().__init__(msg, *args)


class FactoryConfigError(ConfigError):
    pass


class FeederConfigError(ConfigError):
    pass
