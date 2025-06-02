// src/main.ts
import { enableProdMode, importProvidersFrom } from '@angular/core';
import { bootstrapApplication }              from '@angular/platform-browser';
import { provideRouter }                     from '@angular/router';
import { provideHttpClient, HttpClientModule } from '@angular/common/http';

import {
  BaseChartDirective,
  provideCharts,
  withDefaultRegisterables
} from 'ng2-charts';
import { Chart, registerables } from 'chart.js';

import { AppComponent } from './app/app.component';
import { routes }       from './app/app.routes';
import { environment }  from './environments/environment';

if (environment.production) {
  enableProdMode();
}

// Enregistre les controllers, scales, légendes… de Chart.js
Chart.register(...registerables);

bootstrapApplication(AppComponent, {
  providers: [
    // 1) HTTP client
    importProvidersFrom(HttpClientModule),
    provideHttpClient(),

    // 2) Routing
    provideRouter(routes),

    // 3) Chart.js + directive standalone
    provideCharts(withDefaultRegisterables()),
    importProvidersFrom(BaseChartDirective)
  ]
})
.catch(err => console.error(err));
