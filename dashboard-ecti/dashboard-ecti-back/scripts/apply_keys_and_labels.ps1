# apply_keys_and_labels.ps1

# Dictionnaire : fichier → app_label
$mapping = @{
  'api/models_ecti.py'        = 'ecti'
  'api/models_infolocales.py' = 'infolocales'
  'api/models_tablecti.py'    = 'tablecti'
  'api/models_tstatic.py'     = 'tstatic'
}

foreach ($file in $mapping.Keys) {
  Write-Host "`n=== Traitement de $file (`$app_label = $($mapping[$file])) ==="

  # 1) ajoute primary_key=True sur le premier champ de chaque Model
  python tools/fix_primary_key.py $file

  # 2) injecte app_label = '<nom_app>' DANS chaque class Meta
  python tools/add_label.py       $file $mapping[$file]
}

Write-Host "`nPrimary keys et app_label injectés sur tous vos modèles !"
