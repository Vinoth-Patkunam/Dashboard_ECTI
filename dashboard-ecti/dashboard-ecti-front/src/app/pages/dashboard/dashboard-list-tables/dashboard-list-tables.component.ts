import { Component, OnInit, AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { CommonModule }     from '@angular/common';
import { FormsModule }      from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { Chart, ChartConfiguration, ChartType, registerables } from 'chart.js';

import { MultiDbService } from '../../../services/multidb.service';

// Union littérale pour restreindre aux 4 types voulus
type MyChartType = 'bar' | 'line' | 'pie' | 'doughnut';

@Component({
  selector: 'app-dashboard-list-tables',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule
  ],
  templateUrl: './dashboard-list-tables.component.html',
  styleUrls: ['./dashboard-list-tables.component.scss']
})
export class DashboardListTablesComponent implements OnInit, AfterViewInit {
  public allTables: string[] = ['notedefrais', 'affectations', 'conventionfilieres'];
  public searchText: string = '';
  public filteredTables: string[] = [];
  public currentTable: string | null = null;
  public loading: boolean = false;

  public chartTypes: MyChartType[] = ['bar', 'line', 'pie', 'doughnut'];
  public selectedChartType: MyChartType = 'bar';

  @ViewChild('canvasRef') canvasRef!: ElementRef<HTMLCanvasElement>;
  private chartInstance: Chart<'bar'|'line'|'pie'|'doughnut'> | null = null;

  constructor(private multiDbService: MultiDbService) {
    Chart.register(...registerables);
  }

  ngOnInit(): void {
    this.filteredTables = [...this.allTables];
  }

  ngAfterViewInit(): void {}

  public onSearchTextChange(): void {
    const txt = this.searchText.trim().toLowerCase();
    this.filteredTables = txt
      ? this.allTables.filter(tbl => tbl.toLowerCase().includes(txt))
      : [...this.allTables];
  }

  public onTableClick(tableName: string): void {
    this.currentTable = tableName;
    this.buildChartForTable();
  }

  public onChartTypeChange(newType: MyChartType): void {
    this.selectedChartType = newType;
    if (this.currentTable) {
      this.buildChartForTable();
    }
  }

  private buildChartForTable(): void {
    if (!this.currentTable) return;
    this.loading = true;

    this.multiDbService.getData<any>(this.currentTable).subscribe(
      rawData => {
        const aggregation: Map<string, number> = new Map();
        rawData.forEach(item => {
          const dateVal = item['datesaisie'] || item['date_saisie'] || null;
          const montantVal = item['montantpaye'] || item['montant_paye'] || 1;
          if (!dateVal) return;

          let mois: string;
          if (typeof dateVal === 'string' && /^\d{4}-\d{2}-\d{2}T/.test(dateVal)) {
            mois = dateVal.slice(0, 7);
          } else {
            mois = dateVal.toString();
          }

          const num = parseFloat(montantVal);
          if (isNaN(num)) return;
          const prev = aggregation.get(mois) ?? 0;
          aggregation.set(mois, prev + num);
        });

        const labels = Array.from(aggregation.keys()).sort();
        const values = labels.map(lbl => aggregation.get(lbl)!);

        if (this.chartInstance) {
          this.chartInstance.destroy();
          this.chartInstance = null;
        }

        const config: ChartConfiguration<'bar'|'line'|'pie'|'doughnut'> = {
          type: this.selectedChartType,
          data: {
            labels: labels,
            datasets: [
              {
                data: values,
                label: `Données (${this.currentTable})`,
                backgroundColor: this.getRandomColors(labels.length),
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
              }
            ]
          },
          options: {
            responsive: true,
            scales: (this.selectedChartType === 'bar' || this.selectedChartType === 'line')
              ? {
                  x: { title: { display: true, text: 'Mois (YYYY-MM)' } },
                  y: { beginAtZero: true, title: { display: true, text: 'Valeur' } }
                }
              : {},
            plugins: {
              legend: { display: true, position: 'top' },
              tooltip: {
                callbacks: {
                  label: ctx => {
                    const raw = (ctx.parsed as any).y ?? ctx.parsed;
                    const fmt = (typeof raw === 'number')
                      ? raw.toLocaleString('fr-FR', {
                          minimumFractionDigits: 2,
                          maximumFractionDigits: 2
                        })
                      : raw;
                    return this.selectedChartType === 'pie' || this.selectedChartType === 'doughnut'
                      ? `${ctx.label}: ${fmt}`
                      : `€ ${fmt}`;
                  }
                }
              }
            }
          }
        };

        setTimeout(() => {
  const ctx = this.canvasRef?.nativeElement?.getContext('2d');
  if (ctx) {
    this.chartInstance = new Chart(ctx, config);
  }
  this.loading = false;
});


        this.loading = false;
      },
      err => {
        console.error(`Erreur récupération données pour "${this.currentTable}" :`, err);
        this.loading = false;
      }
    );
  }

  private getRandomColors(count: number): string[] {
    const cols: string[] = [];
    for (let i = 0; i < count; i++) {
      const r = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
      const g = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
      const b = Math.floor(Math.random() * 256).toString(16).padStart(2, '0');
      cols.push(`#${r}${g}${b}`);
    }
    return cols;
  }
}
