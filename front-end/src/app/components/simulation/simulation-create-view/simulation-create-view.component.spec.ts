import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationCreateViewComponent } from './simulation-create-view.component';
import {MatCardModule} from '@angular/material/card';
import {FormBuilder, ReactiveFormsModule} from '@angular/forms';
import {HttpClientTestingModule} from '@angular/common/http/testing';
import {MatInputModule} from '@angular/material/input';
import {MatIconModule} from '@angular/material/icon';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {ActivatedRoute, Router} from '@angular/router';
import {RouterTestingModule} from '@angular/router/testing';

describe('SimulationCreateViewComponent', () => {
  let component: SimulationCreateViewComponent;
  let fixture: ComponentFixture<SimulationCreateViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [
        MatCardModule,
        HttpClientTestingModule,
        MatInputModule,
        MatIconModule,
        ReactiveFormsModule,
        BrowserAnimationsModule,
        MatSnackBarModule,
        RouterTestingModule
      ],
      declarations: [ SimulationCreateViewComponent ],
      providers: [
        FormBuilder,
        {
          provide: ActivatedRoute,
          useValue: {}
        }
      ]
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
