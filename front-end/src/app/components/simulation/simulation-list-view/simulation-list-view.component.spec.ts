import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationListViewComponent } from './simulation-list-view.component';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {MatCardModule} from '@angular/material/card';
import {MatIconModule} from '@angular/material/icon';
import {RouterTestingModule} from '@angular/router/testing';

describe('SimulationListViewComponent', () => {
  let component: SimulationListViewComponent;
  let fixture: ComponentFixture<SimulationListViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SimulationListViewComponent ],
      imports: [
        HttpClientTestingModule,
        MatCardModule,
        MatIconModule,
        RouterTestingModule
      ],
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
