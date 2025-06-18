// src/app/app.routes.ts
import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardListTablesComponent } from './pages/dashboard/dashboard-list-tables/dashboard-list-tables.component';
import { AccueilComponent } from './pages/accueil/accueil.component';
import { UsersComponent }        from './pages/users/users.component';
import { ParametreComponent } from './pages/parametre/parametre.component';


const routes: Routes = [
  { path: 'accueil',      component: AccueilComponent },
  { path: 'dashboard',    component: DashboardListTablesComponent },
  { path: 'utilisateurs', component: UsersComponent},
  { path: 'parametre',    component: ParametreComponent },
  { path: '',             redirectTo: '/accueil', pathMatch: 'full' },
  { path: '**',           redirectTo: '/accueil' }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
