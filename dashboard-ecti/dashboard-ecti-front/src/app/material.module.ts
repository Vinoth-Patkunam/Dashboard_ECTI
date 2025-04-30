// src/app/material.module.ts
import { NgModule }            from '@angular/core';
import { MatSidenavModule }    from '@angular/material/sidenav';
import { MatToolbarModule }    from '@angular/material/toolbar';
import { MatIconModule }       from '@angular/material/icon';
import { MatListModule }       from '@angular/material/list';
import { MatButtonModule }     from '@angular/material/button';
import { MatCardModule }       from '@angular/material/card';
import { MatTableModule }      from '@angular/material/table';
import { MatFormFieldModule }  from '@angular/material/form-field';
import { MatInputModule }      from '@angular/material/input';

@NgModule({
  exports: [
    MatSidenavModule,
    MatToolbarModule,
    MatIconModule,
    MatListModule,
    MatButtonModule,
    MatCardModule,
    MatTableModule,
    MatFormFieldModule,
    MatInputModule
  ]
})
export class MaterialModule { }
