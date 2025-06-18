import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule }  from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

interface Adherent {
  numexp: number;  // Numéro expert
  nom:    string;  // Nom
  pays:   string;  // Pays
  copos:  string;  // Code postal
  emel:    string | null;   // email
  telpor:  string | null;   // portable
}

@Component({
  selector: 'app-users',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit {
  adherents: Adherent[] = [];
  filtered:  Adherent[] = [];
  search:    string    = '';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http
      .get<Adherent[]>('/api/tiadhs/?format=json', {
        headers: { 'Accept': 'application/json' }
      })
      .subscribe(
        data => {
          this.adherents = data;
          this.filtered  = [...data];
        },
        err => {
          console.error('Erreur chargement adhérents', err);
        }
      );
  }

  onSearch(): void {
  const lower = this.search.trim().toLowerCase();
  this.filtered = this.adherents.filter(a => {
    const haystack = 
      `${a.nom} ${a.pays} ${a.copos} ${a.emel ?? ''} ${a.telpor ?? ''}`.toLowerCase();
    return haystack.includes(lower);
  });
}

}
