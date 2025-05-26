# → depuis la racine (dashboard-ecti-back)

$aliases = @(
  @{ db='default';      label='ecti'         },
  @{ db='infolocales';  label='infolocales'  },
  @{ db='tablecti';     label='tablecti'     },
  @{ db='tstatic';      label='tstatic'      }
)

foreach ($item in $aliases) {
  $db    = $item.db
  $label = $item.label
  $file  = "api\models_${label}.py"

  Write-Host "`n→ Génération de $file" -ForegroundColor Cyan

  # 1) Dump brut UTF-8
  python manage.py inspectdb --database $db | Out-File $file -Encoding UTF8

  # 2) On ajoute app_label
  python tools\add_label.py $file $label

  # 3) On fixe la clé primaire automatique
  python tools\fix_primary_key.py $file

  # 4) On formate proprement
  python -m black $file --quiet
}

Write-Host "`nModels regenerated successfully!" -ForegroundColor Green
