import { Routes } from '@angular/router';
import { AccueilComponent } from './pages/accueil/accueil.component';
import { DashboardListTablesComponent } from './pages/dashboard/dashboard-list-tables/dashboard-list-tables.component';
import { UsersComponent } from './pages/users/users.component';
import { ParametreComponent } from './pages/parametre/parametre.component';
import { GraphsComponent } from './pages/graphs/graphs.component';

export const routes: Routes = [
  { path: 'accueil',      component: AccueilComponent },
  { path: 'dashboard',    component: DashboardListTablesComponent },
  { path: 'utilisateurs', component: UsersComponent },
  { path: 'parametre',    component: ParametreComponent },
  { path: 'graphs',       component: GraphsComponent },
  { path: '',   redirectTo: 'accueil', pathMatch: 'full' },
  { path: '**', redirectTo: 'accueil' },
];
