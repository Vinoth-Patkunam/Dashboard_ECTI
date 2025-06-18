import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardListTablesComponent } from './dashboard-list-tables.component';

describe('DashboardListTablesComponent', () => {
  let component: DashboardListTablesComponent;
  let fixture: ComponentFixture<DashboardListTablesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DashboardListTablesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DashboardListTablesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
