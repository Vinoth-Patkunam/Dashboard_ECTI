// src/app/pages/users/users.component.ts
import { Component, OnInit }        from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { MatTableModule }            from '@angular/material/table';
import { MatCardModule }             from '@angular/material/card';
import { environment } from '../../../environments/environment';


@Component({
  standalone: true,
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss'],
  imports: [
    HttpClientModule,
    MatTableModule,
    MatCardModule
  ]
})
export class UsersComponent implements OnInit {
  users: any[] = [];                       // ← PROPRIÉTÉ MANQUANTE
  displayedColumns = ['id', 'nom'];        // (optionnel, pour MatTable)

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http
      .get<any[]>(`${environment.apiUrl}/utilisateurs/`)
      .subscribe(data => (this.users = data));
  }
}
