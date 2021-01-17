import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationListViewComponent } from './simulation-list-view.component';

describe('SimulationListViewComponent', () => {
  let component: SimulationListViewComponent;
  let fixture: ComponentFixture<SimulationListViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SimulationListViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SimulationListViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
