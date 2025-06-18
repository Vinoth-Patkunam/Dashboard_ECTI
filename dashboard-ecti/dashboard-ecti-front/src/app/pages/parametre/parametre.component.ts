// src/app/pages/parametre/parametre.component.ts

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-parametre',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="page-parametre">
      <h2>Page Paramètre</h2>
      <p>Configuration de votre application.</p>
    </div>
  `,
  styles: [
    `
      .page-parametre {
        padding: 1rem;
      }
    `
  ]
})
export class ParametreComponent {}
