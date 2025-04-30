import { bootstrapApplication }   from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { provideHttpClient }      from '@angular/common/http';
import { provideRouter }          from '@angular/router';
import { importProvidersFrom }    from '@angular/core';

import { AppComponent } from './app/app.component';
import { routes }       from './app/app.routes';
import { MaterialModule } from './app/material.module';   // garde si tu veux centraliser Angular Material

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    importProvidersFrom(BrowserAnimationsModule, MaterialModule)
  ]
}).catch(err => console.error(err));
