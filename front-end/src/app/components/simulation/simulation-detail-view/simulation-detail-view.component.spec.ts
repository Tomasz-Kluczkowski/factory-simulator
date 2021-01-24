import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationDetailViewComponent } from './simulation-detail-view.component';

describe('SimulationDetailViewComponent', () => {
  let component: SimulationDetailViewComponent;
  let fixture: ComponentFixture<SimulationDetailViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SimulationDetailViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SimulationDetailViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
