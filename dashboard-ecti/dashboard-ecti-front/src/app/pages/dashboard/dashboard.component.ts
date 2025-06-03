// src/app/pages/dashboard/dashboard.component.ts

import { Component, OnInit, ViewChild } from '@angular/core';
import { CommonModule }           from '@angular/common';
import { HttpClientModule }       from '@angular/common/http';

import { ChartData, ChartOptions } from 'chart.js';
import { BaseChartDirective, provideCharts } from 'ng2-charts';

import { NoteDeFraisService, NoteDeFrais } from '../../services/note-de-frais.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,

  // 1) IMPORTS : directive BaseChartDirective, CommonModule, HttpClientModule
  imports: [
    CommonModule,
    HttpClientModule,
    BaseChartDirective
  ],

  // 2) PROVIDERS : factory de ng2-charts pour que BaseChartDirective fonctionne
  providers: [
    provideCharts()
  ],

  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  // ─── 3) Nombre de notes de frais par mois (bar chart) ───
  public barChartData: ChartData<'bar'> = {
    labels: [],
    datasets: [
      {
        data: [],
        label: 'Nombre de notes de frais',
        backgroundColor: 'rgba(30,144,255,0.7)'
      }
    ]
  };
  public barChartOptions: ChartOptions<'bar'> = {
    responsive: true,
    scales: {
      x: {
        title: { display: true, text: 'Mois (YYYY-MM)' },
        ticks: {
          autoSkip: true,
          maxTicksLimit: 12 // par exemple, pour ne garder que 12 labels max
        }
      },
      y: {
        beginAtZero: true,
        title: { display: true, text: 'Nombre de notes' }
      }
    },
    plugins: {
      legend: { display: true, position: 'top' }
    }
  };

  // ─── 4) Montant total par mois (line chart) ───
  public amountChartData: ChartData<'line'> = {
    labels: [],
    datasets: [
      {
        data: [],
        label: 'Montant total versé par mois (€)',
        fill: false,
        borderColor: 'rgba(75,192,192,1)',
        tension: 0.3
      }
    ]
  };
  public amountChartOptions: ChartOptions<'line'> = {
    responsive: true,
    scales: {
      x: {
        title: { display: true, text: 'Mois (YYYY-MM)' },
        ticks: {
          autoSkip: true,
          maxTicksLimit: 12
        }
      },
      y: {
        beginAtZero: true,
        title: { display: true, text: 'Montant (€)' }
      }
    },
    plugins: {
      legend: { display: true, position: 'top' },
      tooltip: {
        callbacks: {
          label: context => {
            const val = context.parsed.y ?? 0;
            return `€ ${val.toLocaleString('fr-FR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
          }
        }
      }
    }
  };

  // ─── 5) Répartition des montants versés par année (pie chart) ───
  public pieChartData: ChartData<'pie'> = {
    labels: [],
    datasets: [
      {
        data: [],
        label: 'Montant total par année',
        backgroundColor: [
          // quelques couleurs variées pour distinguer les années
          '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
          '#FF9F40', '#C9CBCF', '#FF6384', '#36A2EB', '#FFCE56'
        ]
      }
    ]
  };
  public pieChartOptions: ChartOptions<'pie'> = {
    responsive: true,
    plugins: {
      legend: { display: true, position: 'right' },
      tooltip: {
        callbacks: {
          label: context => {
            const label = context.label ?? '';
            const val = context.parsed as number;
            return `${label} : € ${val.toLocaleString('fr-FR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
          }
        }
      }
    }
  };

  // ─── 6) Somme globale de tous les montants (affiché en haut du dashboard) ───
  public totalMontant: number = 0;

  @ViewChild(BaseChartDirective) chart?: BaseChartDirective;

  constructor(private noteService: NoteDeFraisService) {}

  ngOnInit(): void {
    this.noteService.getAll().subscribe(
      (rawNotes: NoteDeFrais[]) => {
        // ──────────────────────────────────────────────────────────────────────────
        // 1) On prépare trois structures d’agrégation :
        //   a) countsParMois    → nombre de notes par mois (ex : { "2009-06": 12, ... })
        //   b) sumParMois       → montant total versé par mois (ex : { "2009-06":  1234.56, ... })
        //   c) sumParAnnee     → montant total versé par année (ex : { "2009":  5678.90, ... })
        //   d) totalMontant     → somme de tous les montants
        // ──────────────────────────────────────────────────────────────────────────

        const countsParMois: Record<string, number> = {};
        const sumParMois:   Record<string, number> = {};
        const sumParAnnee:  Record<string, number> = {};
        let total = 0;

        rawNotes.forEach((note: NoteDeFrais) => {
          // (a) Vérifier qu’on a bien une date et un montant numérique
          if (!note.datesaisie || note.montantpaye === null || note.montantpaye === undefined) {
            return;
          }

          // (b) Extraction du mois “YYYY-MM” et de l’année “YYYY”
          const mois = note.datesaisie.substring(0, 7); // ex : "2009-06"
          const annee = note.datesaisie.substring(0, 4); // ex : "2009"
          const montant = note.montantpaye;

          // (c) Comptage du nombre de notes par mois
          countsParMois[mois] = (countsParMois[mois] ?? 0) + 1;

          // (d) Somme des montants par mois
          sumParMois[mois] = (sumParMois[mois] ?? 0) + montant;

          // (e) Somme des montants par année
          sumParAnnee[annee] = (sumParAnnee[annee] ?? 0) + montant;

          // (f) Somme globale
          total += montant;
        });

        // ──────────────────────────────────────────────────────────────────────────
        // 2) Transformer ces objets en tableaux triés :
        //   - labelsMois   : liste des mois “YYYY-MM” triés
        //   - labelsAnnees : liste des années “YYYY” triées
        //   - valuesCount  : nombre de notes (correspond à barChart)
        //   - valuesSumMois: montant total par mois (pour line chart)
        //   - valuesSumAnn : montant total par année (pour pie chart)
        //   - total        : somme de tous les montants (pour le compteur)
        // ──────────────────────────────────────────────────────────────────────────

        const labelsMois = Object.keys(countsParMois).sort();
        const valuesCount  = labelsMois.map(m => countsParMois[m]);
        const valuesSumMois = labelsMois.map(m => sumParMois[m]);

        const labelsAnnees = Object.keys(sumParAnnee).sort();
        const valuesSumAnn = labelsAnnees.map(a => sumParAnnee[a]);

        // ──────────────────────────────────────────────────────────────────────────
        // 3) On alimente les ChartData existants :
        //    a) Nombre de notes par mois  → barChartData
        //    b) Montant total par mois    → amountChartData
        //    c) Montant total par année   → pieChartData
        //    d) Somme globale             → totalMontant
        // ──────────────────────────────────────────────────────────────────────────

        // a) Bar chart (nombre de notes par mois)
        this.barChartData.labels = labelsMois;
        this.barChartData.datasets[0].data = valuesCount;

        // b) Line chart (montant total par mois)
        this.amountChartData.labels = labelsMois;
        this.amountChartData.datasets[0].data = valuesSumMois;

        // c) Pie chart (montant total par année)
        this.pieChartData.labels = labelsAnnees;
        this.pieChartData.datasets[0].data = valuesSumAnn;

        // d) Somme globale
        this.totalMontant = total;

        // ──────────────────────────────────────────────────────────────────────────
        // 4) Forcer la mise à jour visuelle (update) des trois charts
        // ──────────────────────────────────────────────────────────────────────────
        setTimeout(() => {
          this.chart?.update();     // Met à jour le graphe courant (bar/line/pie).
          // Si besoin, vous pouvez récupérer un ViewChild séparé pour chaque canvas
          // mais en pratique BaseChartDirective lisse déjà la mise à jour des données.
        }, 0);

      },
      (error) => {
        console.error('🛑 Erreur récupération notes :', error);
      }
    );
  }
}
