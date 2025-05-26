class EctiRouter:
    app_label_to_db = {
        'ecti':        'default',      # ou 'ecti' selon tes noms
        'infolocales': 'infolocales',
        'tablecti':    'tablecti',
        'tstatic':     'tstatic',
    }

    def db_for_read(self, model, **hints):
        return self.app_label_to_db.get(model._meta.app_label)

    # on bloque toute écriture
    def db_for_write(self, model, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return False