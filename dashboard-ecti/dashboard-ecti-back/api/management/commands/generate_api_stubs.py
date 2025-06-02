import os
import importlib
import inspect
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import models as django_models

class Command(BaseCommand):
    help = "Génère serializers.py, views.py et urls.py pour TOUS les models_*.py de l'app api"

    def handle(self, *args, **options):
        # 1) On détecte tous les fichiers models_*.py dans api/
        api_dir = os.path.join(settings.BASE_DIR, "api")
        model_files = [
            f for f in os.listdir(api_dir)
            if f.startswith("models_") and f.endswith(".py")
        ]

        # 2) On importe chaque module et on y extrait les classes Model
        all_models = []
        for filename in model_files:
            module_name = "api." + filename[:-3]  # ex: "api.models_ecti"
            try:
                module = importlib.import_module(module_name)
            except Exception as e:
                self.stdout.write(self.style.WARNING( f"⚠️  Impossible d’importer {module_name} : {e}" ))
                continue
            for attr_name, obj in vars(module).items():
                if (
                    inspect.isclass(obj)
                    and issubclass(obj, django_models.Model)
                    and obj is not django_models.Model
                    and not getattr(obj._meta, 'abstract', False)
                ):
                    all_models.append(obj)

        # 3) On trie par nom de classe
        all_models.sort(key=lambda m: m.__name__)

        # 4) Chemins vers les fichiers qu'on va (ré)écrire
        serializers_file = os.path.join(api_dir, "serializers.py")
        views_file       = os.path.join(api_dir, "views.py")
        urls_file        = os.path.join(api_dir, "urls.py")

        # 5) Génère serializers.py
        with open(serializers_file, "w", encoding="utf-8") as f:
            f.write("from rest_framework import serializers\n\n")
            # imports
            for m in all_models:
                module = m.__module__.split(".")[-1]
                f.write(f"from .{module} import {m.__name__}\n")
            f.write("\n\n")
            # classes
            for m in all_models:
                f.write(f"class {m.__name__}Serializer(serializers.ModelSerializer):\n")
                f.write("    class Meta:\n")
                f.write(f"        model = {m.__name__}\n")
                f.write("        fields = '__all__'\n\n\n")
        self.stdout.write(self.style.SUCCESS(f"→ {serializers_file} généré."))

        # 6) Génère views.py
        with open(views_file, "w", encoding="utf-8") as f:
            f.write("from rest_framework import viewsets\n\n")
            # imports
            for m in all_models:
                module = m.__module__.split(".")[-1]
                f.write(f"from .{module} import {m.__name__}\n")
            f.write("from .serializers import (\n")
            for m in all_models:
                f.write(f"    {m.__name__}Serializer,\n")
            f.write(")\n\n")
            # viewsets
            for m in all_models:
                f.write(f"class {m.__name__}ViewSet(viewsets.ReadOnlyModelViewSet):\n")
                f.write(f"    queryset = {m.__name__}.objects.all()\n")
                f.write(f"    serializer_class = {m.__name__}Serializer\n\n\n")
        self.stdout.write(self.style.SUCCESS(f"→ {views_file} généré."))

        # 7) Génère urls.py
        with open(urls_file, "w", encoding="utf-8") as f:
            f.write("from rest_framework.routers import DefaultRouter\n")
            f.write("from .views import (\n")
            for m in all_models:
                f.write(f"    {m.__name__}ViewSet,\n")
            f.write(")\n\n")
            f.write("router = DefaultRouter()\n")
            for m in all_models:
                route = m.__name__.lower() + "s"
                f.write(f"router.register(r'{route}', {m.__name__}ViewSet, basename='{route}')\n")
            f.write("\nurlpatterns = router.urls\n")
        self.stdout.write(self.style.SUCCESS(f"→ {urls_file} généré."))

        self.stdout.write(self.style.SUCCESS("✅ Tous les fichiers API ont été générés !"))
