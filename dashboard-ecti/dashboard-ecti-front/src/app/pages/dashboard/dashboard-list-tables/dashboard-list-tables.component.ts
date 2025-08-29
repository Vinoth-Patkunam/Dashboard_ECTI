import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { CommonModule }     from '@angular/common';
import { FormsModule }      from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { Chart, ChartConfiguration, registerables } from 'chart.js';
import { MultiDbService }   from '../../../services/multidb.service';
import { CdkTable } from '@angular/cdk/table';

type MyChartType = 'bar'|'line'|'pie'|'doughnut';

@Component({
  selector: 'app-dashboard-list-tables',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './dashboard-list-tables.component.html',
  styleUrls: ['./dashboard-list-tables.component.scss']
})
export class DashboardListTablesComponent implements OnInit {
  public allTables:      string[]      = [];
  public filteredTables: string[]      = [];
  public searchText = '';

  public currentTable: string | null = null;
  public rawData: any[]      = [];
  public columns: string[]   = [];

  public showChart = false;
  public chartTypes: MyChartType[] = ['bar','line','pie','doughnut'];
  public selectedChartType: MyChartType = 'bar';
  public chartLabels:  string[] = [];
  public chartValues:  number[] = [];

  @ViewChild('canvasRef') canvasRef!: ElementRef<HTMLCanvasElement>;
  private chartInstance: Chart | null = null;

  constructor(private svc: MultiDbService) {
    Chart.register(...registerables);
  }

  ngOnInit(): void {
    this.svc.getApiRoot().subscribe(root => {
      this.allTables      = Object.keys(root);
      this.filteredTables = [...this.allTables];
    });
  }

  onSearchTextChange() {
    const txt = this.searchText.trim().toLowerCase();
    this.filteredTables = txt
      ? this.allTables.filter(t => t.toLowerCase().includes(txt))
      : [...this.allTables];
  }
  onTableClick(table: string) {
    this.currentTable = table;
    this.showChart    = false;
    this.rawData      = [];
    this.columns      = [];
    // charger les données brutes
    this.svc.getData<any>(table).subscribe(data => {
      this.rawData = data;
      if (data.length) {
        this.columns = Object.keys(data[0]);
      }
    });
  }

  onShowChart() {
    this.showChart = true;
    this.buildChart();
  }

  onChartTypeChange(t: MyChartType) {
    this.selectedChartType = t;
    if (this.showChart) this.buildChart();
  }

  private buildChart() {
    if (!this.currentTable) return;
    // re-agréger sur datesaisie / montantpaye si présents
    const agg = new Map<string,number>();
    this.rawData.forEach(item => {
      const d = item['datesaisie']||item['date_saisie'];
      const m = parseFloat(item['montantpaye']||item['montant_paye']||'0');
      if (!d || isNaN(m)) return;
      const month = (typeof d=='string' && /^\d{4}-\d{2}-\d{2}/.test(d))
        ? d.slice(0,7)
        : d.toString();
      agg.set(month, (agg.get(month)||0)+m);
    });

    this.chartLabels = Array.from(agg.keys()).sort();
    this.chartValues = this.chartLabels.map(l => agg.get(l)!);

    // détruire ancien chart
    this.chartInstance?.destroy();

    const cfg: ChartConfiguration = {
      type: this.selectedChartType,
      data: {
        labels: this.chartLabels,
        datasets: [{
          label: `Données (${this.currentTable})`,
          data: this.chartValues,
          backgroundColor: this.chartLabels.map(_=>`rgba(75,192,192,0.5)`),
          borderColor: `rgba(75,192,192,1)`,
          borderWidth: 1
        }]
      },
      options: { responsive:true }
    };

    // petit setTimeout pour être sûr que canvas est là
    setTimeout(()=>{
      const ctx = this.canvasRef.nativeElement.getContext('2d')!;
      this.chartInstance = new Chart(ctx, cfg);
    },0);
  }
}
