// src/app/pages/accueil/accueil.component.ts

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-accueil',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="page-accueil">
      <h2>Page Accueil</h2>
      <p>Bienvenue sur l’application Dashboard ECTI !</p>
    </div>
  `,
  styles: [
    `
      .page-accueil {
        padding: 1rem;
      }
    `
  ]
})
export class AccueilComponent {}
