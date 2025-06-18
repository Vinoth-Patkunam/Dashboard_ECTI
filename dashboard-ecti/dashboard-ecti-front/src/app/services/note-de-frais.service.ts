// src/app/services/note-de-frais.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface NoteDeFrais {
  id: number;
  nummission: number;
  expert: number;
  datesaisie: string | null;
  montantpaye: number | null;
}

@Injectable({
  providedIn: 'root'
})
export class NoteDeFraisService {
  private apiUrl = '/api/notedefrais/?format=json';

  constructor(private http: HttpClient) {}

  getAll(): Observable<any[]> {
  return this.http.get<any[]>(this.apiUrl, {
    headers: { 'Accept': 'application/json' }
  });
}
}
