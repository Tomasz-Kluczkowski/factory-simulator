import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationDetailViewComponent } from './simulation-detail-view.component';
import {ActivatedRoute} from '@angular/router';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {of} from 'rxjs';

describe('SimulationDetailViewComponent', () => {
  let component: SimulationDetailViewComponent;
  let fixture: ComponentFixture<SimulationDetailViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      declarations: [ SimulationDetailViewComponent ],
      providers: [
        {
          provide: ActivatedRoute,
          useValue: {
            paramMap: of({})
          }
        }
      ]

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
