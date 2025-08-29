import { Component, AfterViewInit, ElementRef, ViewChild, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { Chart, registerables } from 'chart.js';
import { forkJoin, firstValueFrom } from 'rxjs';

type DashboardPayload = { dep: DepRow[]; aff: AffRow[]; km: KmRow[] };
type DepRow = { depar: string; total: number };
type AffRow = { annee: string | number; total: number };
type KmRow  = { annee: string | number; km: number };

@Component({
  standalone: true,
  selector: 'app-graphs',
  templateUrl: './graphs.component.html',
  imports: [CommonModule, HttpClientModule],
})
export class GraphsComponent implements AfterViewInit, OnDestroy {
  @ViewChild('dep') dep!: ElementRef<HTMLCanvasElement>;
  @ViewChild('aff') aff!: ElementRef<HTMLCanvasElement>;
  @ViewChild('km')  km!:  ElementRef<HTMLCanvasElement>;

  private charts: Chart[] = [];
  error = '';

  constructor(private http: HttpClient) {
    Chart.register(...registerables);
  }

async ngAfterViewInit() {
  try {
    const all = await firstValueFrom(
      this.http.get<DashboardPayload>('/api/stats/dashboard/')
    );

    const dep = all.dep ?? [];
    const aff = all.aff ?? [];
    const km  = all.km  ?? [];

    this.destroyCharts();

    // Graph 1 : par département
    this.charts.push(new Chart(this.dep.nativeElement.getContext('2d')!, {
      type: 'bar',
      data: { labels: dep.map(d=>d.depar || 'ND'),
              datasets: [{ label: 'Affectations', data: dep.map(d=>d.total) }] },
      options: { responsive: true }
    }));

    // Graph 2 : affectations / année
    this.charts.push(new Chart(this.aff.nativeElement.getContext('2d')!, {
      type: 'line',
      data: { labels: aff.map(d=>d.annee),
              datasets: [{ label: 'Affectations', data: aff.map(d=>d.total), tension: 0.2 }] },
      options: { responsive: true }
    }));

    // Graph 3 : km / année
    this.charts.push(new Chart(this.km.nativeElement.getContext('2d')!, {
      type: 'line',
      data: { labels: km.map(d=>d.annee),
              datasets: [{ label: 'Km', data: km.map(d=>d.km), tension: 0.2 }] },
      options: { responsive: true }
    }));
  } catch (e) {
    console.error(e);
    this.error = 'Impossible de charger les statistiques.';
  }
}

  ngOnDestroy() {
    this.destroyCharts();
  }

  private destroyCharts() {
    this.charts.forEach(c => c.destroy());
    this.charts = [];
  }
}
