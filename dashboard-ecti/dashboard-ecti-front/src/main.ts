import { bootstrapApplication } from '@angular/platform-browser';
import {
  provideRouter,
  withEnabledBlockingInitialNavigation,
  Routes
} from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { AppComponent } from './app/app.component';
import { AccueilComponent } from './app/pages/accueil/accueil.component';
import { ParametreComponent } from './app/pages/parametre/parametre.component';

const routes: Routes = [
  { path: 'accueil', component: AccueilComponent },

  {
    path: 'dashboard',
    loadComponent: () =>
      import('./app/pages/dashboard/dashboard-list-tables/dashboard-list-tables.component')
        .then(m => m.DashboardListTablesComponent)
  },
  {
    path: 'utilisateurs',
    loadComponent: () =>
      import('./app/pages/users/users.component').then(m => m.UsersComponent)
  },
  { path: 'parametre', component: ParametreComponent },

  {
    path: 'graphs',
    loadComponent: () =>
      import('./app/pages/graphs/graphs.component').then(m => m.GraphsComponent)
  },

  { path: '',   redirectTo: 'accueil', pathMatch: 'full' },
  { path: '**', redirectTo: 'accueil' }
];

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes, withEnabledBlockingInitialNavigation()),
    provideHttpClient()
  ]
}).catch(err => console.error(err));