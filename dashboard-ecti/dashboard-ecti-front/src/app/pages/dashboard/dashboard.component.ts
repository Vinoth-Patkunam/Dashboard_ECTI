// src/app/pages/dashboard/dashboard.component.ts

import { Component, OnInit } from '@angular/core';
import { HttpClientModule }   from '@angular/common/http';
import { ApiService }         from '../../services/api.service';
import { ChartData, ChartOptions } from 'chart.js';
import { BaseChartDirective } from 'ng2-charts';

interface NoteDeFrais { statut: number; montanttotal: number; }

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    HttpClientModule,   // ← pour ApiService
    BaseChartDirective  // ← pour <canvas baseChart>
  ],
  template: `
    <div style="width:70%; margin:auto">
      <canvas baseChart
              [data]="barChartData"
              [options]="barChartOptions"
              chartType="bar">
      </canvas>
    </div>
  `
})
export class DashboardComponent implements OnInit {
  public barChartOptions: ChartOptions<'bar'> = {
    responsive: true,
    scales: {
      y: { beginAtZero: true }
    }
  };
  public barChartData: ChartData<'bar'> = {
    labels: [],
    datasets: [{ data: [], label: 'Montant total par statut' }]
  };

  constructor(private api: ApiService) {}

  ngOnInit(): void {
    this.api.getAll<NoteDeFrais>('notedefrais')
      .subscribe(data => {
        console.log('raw data:', data);   // <=== vérifie bien le JSON
        const sums = data.reduce((acc, cur) => {
          acc[cur.statut] = (acc[cur.statut] || 0) + cur.montanttotal;
          return acc;
        }, {} as Record<number, number>);
        console.log('aggregated sums:', sums);

        this.barChartData.labels  = Object.keys(sums).map(k => `Statut ${k}`);
        this.barChartData.datasets[0].data = Object.values(sums);
        console.log('chart labels:', this.barChartData.labels);
        console.log('chart data:', this.barChartData.datasets[0].data);
      }, err => console.error(err));
  }
}

