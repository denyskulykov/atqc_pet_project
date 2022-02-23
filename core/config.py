import configparser
import os

SETTINGS_FILE_PATH = 'settings.ini'


def get_project_root():
    return os.path.realpath(os.getcwd())


class Settings:
    def __init__(self):
        self._configured = False

        self.host = None
        self.user = None
        self.password = None

        self.log_path = None
        self.log_mode = None
        self.verbosity = None

    @property
    def configured(self):
        return self._configured

    def configure(self):

        settings_path = os.path.join(get_project_root(), SETTINGS_FILE_PATH)
        if not os.path.isfile(settings_path):
            raise Exception('Not able to find settings file at {}'.format(settings_path))

        config = configparser.ConfigParser()
        config.read(settings_path)

        self.host = config['rest']['host']
        self.user = config['rest']['username']
        self.password = config['rest']['password']

        self.log_path = os.path.join(get_project_root(), config['general']['log_path'])
        self.log_mode = config['general']['log_mode']
        self.verbosity = config['general']['verbosity']

        self._configured = True
