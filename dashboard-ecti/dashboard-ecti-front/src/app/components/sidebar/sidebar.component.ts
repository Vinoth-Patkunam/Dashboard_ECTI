// src/app/components/sidebar/sidebar.component.ts
import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';


// src/app/components/sidebar/sidebar.component.ts
@Component({
  standalone: true,
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss'],
  imports: [MatListModule, MatIconModule, RouterLink, RouterLinkActive]
})
export class SidebarComponent {}
