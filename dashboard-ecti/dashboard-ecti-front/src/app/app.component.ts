// src/app/app.component.ts
import { Component } from '@angular/core';

import { RouterOutlet, RouterModule } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule }    from '@angular/material/icon';
import { MatListModule }    from '@angular/material/list';

import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HeaderComponent } from './components/header/header.component';

@Component({
  standalone: true,
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  imports: [
    RouterOutlet, RouterModule,
    MatSidenavModule, MatToolbarModule, MatIconModule, MatListModule,
    SidebarComponent,
    HeaderComponent 
  ]
})
export class AppComponent {}
