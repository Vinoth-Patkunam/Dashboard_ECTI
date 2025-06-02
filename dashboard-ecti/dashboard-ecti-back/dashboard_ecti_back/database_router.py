class ECTIRouter:
    def db_for_read(self, model, **hints):
        if getattr(model._meta, "app_label", "") in ("ecti", "infolocales", "tablecti", "tstatic"):
            return model._meta.app_label  # ecti, infolocales, etc.
        return "default"

    def db_for_write(self, model, **hints):
        # On ne fait pas d'écriture sur les bases MySQL
        return "default"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Autorise les migrations uniquement sur default (sqlite)
        return db == "default"
