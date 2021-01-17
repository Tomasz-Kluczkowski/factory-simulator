import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationCreateViewComponent } from './simulation-create-view.component';

describe('SimulationCreateViewComponent', () => {
  let component: SimulationCreateViewComponent;
  let fixture: ComponentFixture<SimulationCreateViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SimulationCreateViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SimulationCreateViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
