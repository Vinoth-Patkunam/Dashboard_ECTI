# fix_all_models.ps1

# 0) UTF-8 déjà forcé plus haut
# 1) Liste des DB → fichier cible → app_label
$dbs = @(
  @{ name='default';       file='api/models_ecti.py';        label='ecti'       },
  @{ name='infolocales';   file='api/models_infolocales.py'; label='infolocales'},
  @{ name='tablecti';      file='api/models_tablecti.py';    label='tablecti'   },
  @{ name='tstatic';       file='api/models_tstatic.py';     label='tstatic'    }
)

foreach ($db in $dbs) {
  Write-Host "`n>>> Génération pour DB '$($db.name)'"

  # a) inspectdb → UTF-8
  python manage.py inspectdb --database $($db.name) `
    | Out-File -FilePath $($db.file) -Encoding utf8

  # b) normalize_models.py : retire BOM, caractères non-imprimables, uniformise tabs…
  python tools/normalize_models.py $($db.file)

  # c) fix_models.py     : strip accents, ascii-only, tabs→4 espaces, prépare app_label
  python tools/fix_models.py $($db.file)

  # d) fix_primary_key.py: ajoute primary_key=True au premier champ
  python tools/fix_primary_key.py $($db.file)

  # e) add_label.py      : injecte app_label dans chaque class Meta
  python tools/add_label.py $($db.file) $($db.label)
}

Write-Host "`nTous les modèles ont été régénérés et corrigés."
