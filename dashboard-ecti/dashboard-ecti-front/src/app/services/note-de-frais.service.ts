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

@Injectable({ providedIn: 'root' })
export class NoteDeFraisService {
  // Make sure d’appeler bien l’URL avec le slash final
  private baseUrl = '/api/notedefrais/';

  constructor(private http: HttpClient) {}

  getAll(): Observable<NoteDeFrais[]> {
    return this.http.get<NoteDeFrais[]>(this.baseUrl);
  }
}
