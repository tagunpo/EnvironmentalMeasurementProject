DATABASE_MAPPING = {
    'EnvironmentalMeasurementProject': 'default',
    'TecrisDB': 'TecrisDB',
    'PublicDB': 'PublicDB',
    'MlitDB': 'MlitDB',
    'DamDB': 'DamDB',
    'RiverDB': 'RiverDB',
    'WisefDB': 'WisefDB',
}
class EnvironmentalMeasurementProjectDBRouter:

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return DATABASE_MAPPING.get(app_label) == db


    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'EnvironmentalMeasurementProject':
            return 'default'
        elif model._meta.app_label == 'TecrisDB':
            return 'TecrisDB'
        elif model._meta.app_label == 'PublicDB':
            return 'PublicDB'
        elif model._meta.app_label == 'MlitDB':
            return 'MlitDB'
        elif model._meta.app_label == 'DamDB':
            return 'DamDB'
        elif model._meta.app_label == 'RiverDB':
            return 'RiverDB'
        elif model._meta.app_label == 'WisefDB':
            return 'WisefDB'
        else:
            return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'EnvironmentalMeasurementProject':
            return 'default'
        elif model._meta.app_label == 'TecrisDB':
            return 'TecrisDB'
        elif model._meta.app_label == 'PublicDB':
            return 'PublicDB'
        elif model._meta.app_label == 'MlitDB':
            return 'MlitDB'
        elif model._meta.app_label == 'DamDB':
            return 'DamDB'
        elif model._meta.app_label == 'RiverDB':
            return 'RiverDB'
        elif model._meta.app_label == 'WisefDB':
            return 'WisefDB'
        else:
            return 'default'
